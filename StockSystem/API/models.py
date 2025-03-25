from django.db import models
from django.utils import timezone
from django.db.models import Sum

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)  # SKU for stock tracking
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    available_size = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    reorder_level = models.PositiveIntegerField(default=10)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.name

# Stock Model
class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="stock")
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} in stock"

# Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

# Order Model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"

# Sales Model
class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="sales")
    quantity_sold = models.PositiveIntegerField()
    sku = models.CharField(max_length=50)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], default='Completed')

    def __str__(self):
        return f"{self.quantity_sold} x {self.product.name} - {self.sale_price}"

# Stock History Model (Tracks stock changes)
class StockHistory(models.Model):
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=50, choices=[('Restock', 'Restock'), ('Sale', 'Sale')])
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="stock_history")
    sku = models.CharField(max_length=50)
    stock_change = models.IntegerField()
    starting_stock = models.PositiveIntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.transaction_type} - {self.product.name} - {self.stock_change}"

# Restock Request Model
class RestockRequest(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="restock_requests")
    requested_quantity = models.PositiveIntegerField()
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
        return f"Restock Request for {self.product.name} - {self.status}"
