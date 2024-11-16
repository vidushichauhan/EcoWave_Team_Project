from django.contrib import admin
from .models import Product,Reviews
# Register your models here.
admin.site.register(Reviews)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_verified', 'in_stock', 'created_at')
    list_editable = ('is_verified',)
    list_filter = ('is_verified', 'in_stock', 'created_at')
