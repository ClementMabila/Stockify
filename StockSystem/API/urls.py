from django.urls import path
from . import views
from .views import StockAlertViewSet, UploadCSVView, SalesEntryViewSet, StockHistoryViewSet, InventoryViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stock-alerts', StockAlertViewSet, basename='stock-alert')
router.register(r'sales-entries', SalesEntryViewSet, basename='sales-entry')
router.register(r'stock-history', StockHistoryViewSet, basename='stock-history')
router.register(r'inventory', InventoryViewSet, basename='inventory')

urlpatterns = [
    path('api/set-csrf-token', views.set_csrf_token, name='set_csrf_token'),
    path('api/login', views.login_view, name='login'),
    path('api/logout', views.logout_view, name='logout'),
    path('api/user', views.user, name='user'),
    path('api/register', views.register, name='register'),
    path('api/', include(router.urls)),
    path('api/upload-csv/', UploadCSVView.as_view(), name='upload-csv'),
]