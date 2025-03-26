import json
import csv
from io import TextIOWrapper
import pandas as pd
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import CreateUserForm
from .models import RestockRequest, Sale, StockHistory, Product
from .serializers import (
    StockAlertSerializer,
    SalesEntrySerializer,
    StockHistorySerializer,
    InventorySerializer,
)

@ensure_csrf_cookie
@require_http_methods(['GET'])
def set_csrf_token(request):
    """
    We set the CSRF cookie on the frontend.
    """
    return JsonResponse({'message': 'CSRF cookie set'})

@require_http_methods(['POST'])
def login_view(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        email = data['email']
        password = data['password']
    except json.JSONDecodeError:
        return JsonResponse(
            {'success': False, 'message': 'Invalid JSON'}, status=400
        )

    user = authenticate(request, username=email, password=password)

    if user:
        login(request, user)
        return JsonResponse({'success': True})
    return JsonResponse(
        {'success': False, 'message': 'Invalid credentials'}, status=401
    )

def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out'})

@require_http_methods(['GET'])
def user(request):
    if request.user.is_authenticated:
        return JsonResponse(
            {'username': request.user.username, 'email': request.user.email}
        )
    return JsonResponse(
        {'message': 'Not logged in'}, status=401
    )

@require_http_methods(['POST'])
def register(request):
    data = json.loads(request.body.decode('utf-8'))
    form = CreateUserForm(data)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': 'User registered successfully'}, status=201)
    else:
        errors = form.errors.as_json()
        return JsonResponse({'error': errors}, status=400)
    
class StockAlertViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StockAlertSerializer
    def get_queryset(self):
        queryset = RestockRequest.objects.filter(requested_quantity__lte=999999)
        return queryset
    
class SalesEntryViewSet(viewsets.ModelViewSet):  # Change from ReadOnlyModelViewSet
    queryset = Sale.objects.all().order_by('-sale_date')
    serializer_class = SalesEntrySerializer
    
class StockHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StockHistory.objects.all().order_by('-transaction_date') 
    serializer_class = StockHistorySerializer

class InventoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = InventorySerializer

class UploadCSVView(APIView):
    def post(self, request):
        if 'csv_file' not in request.FILES:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        csv_file = request.FILES['csv_file']

        try:
            df = pd.read_csv(csv_file)

            required_columns = ['product_id', 'transaction_type', 'sku', 'stock_change', 'starting_stock', 'total_revenue']
            if not all(col in df.columns for col in required_columns):
                return Response({'error': 'CSV file is missing required columns'}, status=status.HTTP_400_BAD_REQUEST)

            for index, row in df.iterrows():
                try:
                    product = Product.objects.get(id=row['product_id'])
                    stock_change = int(row['stock_change'])
                    starting_stock = int(row['starting_stock'])
                    total_revenue = float(row['total_revenue'])

                    StockHistory.objects.create(
                        transaction_type=row['transaction_type'],
                        product=product,
                        sku=row['sku'],
                        stock_change=stock_change,
                        starting_stock=starting_stock,
                        total_revenue=total_revenue,
                    )
                except Product.DoesNotExist:
                    return Response({'error': f"Product with ID {row['product_id']} not found"}, status=status.HTTP_400_BAD_REQUEST)
                except ValueError as e:
                    return Response({'error': f"Invalid data in CSV file: {e}"}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': 'CSV data uploaded successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f"Error processing CSV: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)