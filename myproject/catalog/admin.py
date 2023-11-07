from django.contrib import admin
from .models import Product, Category
from django.contrib import admin
from .models import Version

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

class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_title', 'is_current')  # поля, которые будут отображаться в списке
    list_filter = ('product', 'is_current')  # фильтры по полям
    search_fields = ('version_number', 'version_title')

admin.site.register(Version, VersionAdmin)