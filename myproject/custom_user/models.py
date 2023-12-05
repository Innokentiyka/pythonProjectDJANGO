from django.db import models
from django.shortcuts import render
from .models import Client
from django.contrib.auth.models import AbstractUser


class Client(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=100)
    comment = models.TextField()

class Newsletter(models.Model):
    START_TIME_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('created', 'Created'),
        ('running', 'Running'),
    ]

    start_time = models.DateTimeField()
    frequency = models.CharField(max_length=10, choices=START_TIME_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

class Message(models.Model):
    subject = models.CharField(max_length=100)
    body = models.TextField()
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)

class Log(models.Model):
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    response = models.TextField()

def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'clients_list.html', {'clients': clients})

class EmailLog(models.Model):
    # Ссылка на конкретное сообщение, если это уместно
    message = models.ForeignKey('Message', on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    recipient_email = models.EmailField()  # Email получателя
    status = models.CharField(max_length=100)  # Например, 'Успешно', 'Ошибка'
    response = models.TextField(blank=True, null=True)  # Ответ от сервера или описание ошибки

    def str(self):
        return f"{self.recipient_email} - {self.status} - {self.timestamp}"

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Дополнительные поля для пользователя
    # Например, для подтверждения почты
    email_confirmed = models.BooleanField(default=False)