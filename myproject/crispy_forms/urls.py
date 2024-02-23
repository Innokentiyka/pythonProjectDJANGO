from django.urls import path
from .views import (
    client_list, client_create, client_edit, client_delete,
    mailing_list, mailing_create, mailing_edit, mailing_delete
)

urlpatterns = [
    # Пути для клиентов
    path('clients/', client_list, name='client_list'),
    path('clients/add/', client_create, name='client_create'),
    path('clients/<int:pk>/edit/', client_edit, name='client_edit'),
    path('clients/<int:pk>/delete/', client_delete, name='client_delete'),

    # Пути для рассылок
    path('mailings/', mailing_list, name='mailing_list'),
    path('mailings/add/', mailing_create, name='mailing_create'),
    path('mailings/<int:pk>/edit/', mailing_edit, name='mailing_edit'),
    path('mailings/<int:pk>/delete/', mailing_delete, name='mailing_delete'),
]