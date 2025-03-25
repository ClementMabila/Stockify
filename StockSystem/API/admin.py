from django.contrib import admin
from .models import Supplier, Product, Stock, Customer, Order, Sale, StockHistory, RestockRequest

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'email')
    search_fields = ('name', 'email')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'sku', 'unit_price', 'supplier')
    search_fields = ('name', 'sku')
    list_filter = ('category',)

class StockAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')
    search_fields = ('product__name',)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'total_amount')
    search_fields = ('customer__name',)
    list_filter = ('order_date',)

class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'quantity_sold', 'sale_price', 'sale_date', 'status')
    search_fields = ('product__name', 'customer__name')
    list_filter = ('sale_date', 'status')

class StockHistoryAdmin(admin.ModelAdmin):
    list_display = ('transaction_date', 'transaction_type', 'product', 'stock_change', 'starting_stock', 'total_revenue')
    search_fields = ('product__name', 'sku')
    list_filter = ('transaction_type',)

class RestockRequestAdmin(admin.ModelAdmin):
    list_display = ('product', 'requested_quantity', 'request_date', 'status')
    search_fields = ('product__name',)
    list_filter = ('status',)

# Register your models with the custom admin classes
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(StockHistory, StockHistoryAdmin)
admin.site.register(RestockRequest, RestockRequestAdmin)
