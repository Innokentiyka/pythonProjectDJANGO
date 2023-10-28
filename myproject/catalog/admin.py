from django.contrib import admin
from .models import Product, Category

from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')

admin.site.register(Product, ProductAdmin)

