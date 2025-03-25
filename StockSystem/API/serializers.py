from rest_framework import serializers
from .models import  Sale, StockHistory, Product, RestockRequest
from django.db.models import Sum

class StockAlertSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name')  # Access the 'name' field of the related Product
    sku = serializers.CharField(source='product.sku')      # Access the 'sku' field of the related Product

    class Meta:
        model = RestockRequest
        fields = ['request_date', 'product', 'sku', 'requested_quantity', 'status']


class SalesEntrySerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name')
    sku = serializers.CharField(source='product.sku') 

    class Meta:
        model = Sale
        fields = ['sale_date', 'product', 'sku', 'quantity_sold', 'sale_price', 'status']


class StockHistorySerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name')
    sku = serializers.CharField(source='product.sku') 

    class Meta:
        model = StockHistory
        fields = ['transaction_date', 'transaction_type', 'product', 'sku', 'stock_change', 'starting_stock', 'total_revenue']


class InventorySerializer(serializers.ModelSerializer):
    total_revenue = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'category', 'sku', 'available_size', 'unit_price', 'location', 'reorder_level', 'total_revenue']

    def get_total_revenue(self, obj):
        total_revenue = Sale.objects.filter(product=obj).aggregate(Sum('sale_price'))['sale_price__sum']
        return total_revenue if total_revenue else 0