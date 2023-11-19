from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    # ...
    path('product/<int:pk>/', cache_page(60*15)(views.product_detail), name='product_detail'),
    # ...
]