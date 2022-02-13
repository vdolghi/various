from tkinter.tix import Tree
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='staticfiles/images/avatars/')
    birth_date = models.DateField
    class Meta:
        db_table = 'tbl_users'

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = CountryField()
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=20)
    phone = PhoneNumberField(blank=True)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_addresses'
class Product(models.Model):
    class Category(models.TextChoices):
        RED = 'red', 'Red Wine'
        WHITE = 'white', 'White Wine'
        ROSE = 'rose', 'Rosé Wine'


    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(default='')
    category = models.CharField(max_length=5, choices=Category.choices, default=Category.RED)
    vendor = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    stock = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'tbl_products'
        ordering = ('name',)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='staticfiles/images/products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'tbl_product_images'

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField
    rating = models.SmallIntegerField(default=None, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'tbl_product_reviews'
        unique_together = ['product','user']

class Order(models.Model):
    class OrderStatus(models.TextChoices):
        NEW = 'new', 'New order before payment'
        PAYMENT_CONFIRMED = 'payment_confirmed', 'New order after payment confirmation'
        IN_PROGRESS = 'in_progress', 'Order being processed'
        COMPLETED = 'completed', 'Order completed'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'tbl_orders'

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    single_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'tbl_order_details'
