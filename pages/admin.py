from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import CustomUserCreationForm, CustomUserChangeForm
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email', 'is_staff', 'first_name','last_name', 'birth_date','avatar' ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('birth_date','avatar',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('email', 'is_staff', 'first_name','last_name','birth_date','avatar',)}),)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Address)

class ProductReviewInline(admin.TabularInline):
    model = ProductReview
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): 
    list_display = ('name' , 'category' , 'slug' , 'vendor', 'price' , 'discount', 'stock') 
    list_filter = ('category', 'price', 'stock') 
    prepopulated_fields = {'slug':('name',)} 
    inlines = [ProductReviewInline]

admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(Order)
admin.site.register(OrderDetails)