from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    path('products/', views.product_list, name='product_list'),


    path('product/<int:pk>/', views.product_detail, name='product_detail'),


    path('product/edit/<int:pk>/', views.edit_product, name='edit_product'),


    path('product/change-status/<int:pk>/', views.change_product_status, name='change_product_status'),
]