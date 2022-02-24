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
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(Order)
admin.site.register(OrderDetails)