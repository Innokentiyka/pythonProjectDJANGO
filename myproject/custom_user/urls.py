from . import views
from .views import clients_list
from django.urls import path
from .views import register, activate


urlpatterns = [
    path('clients/', clients_list, name='clients_list'),

    path('clients/', views.clients_list, name='clients_list'),

    # Путь к странице добавления нового клиента
    path('clients/add/', views.add_client, name='add_client'),

    # Путь к странице редактирования клиента
    path('clients/edit/<int:id>/', views.edit_client, name='edit_client'),

    # Путь к странице деталей рассылки
    path('newsletter/<int:id>/', views.newsletter_detail, name='newsletter_detail'),
    path('register/', register, name='register'),

    path('activate/<uidb64>/<token>/', activate, name='activate'),
]


