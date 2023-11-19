from django.core.cache import cache
from .models import Category

def get_cached_categories():
    if 'categories' in cache:
        return cache.get('categories')
    else:
        categories = Category.objects.all()
        cache.set('categories', categories, 60*60)  # Кешируем на 1 час
        return categories