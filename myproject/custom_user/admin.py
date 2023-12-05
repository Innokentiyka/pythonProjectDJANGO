from django.contrib import admin
from .models import Client, Newsletter, Message, Log

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'comment']
    search_fields = ['email', 'full_name']

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['start_time', 'frequency', 'status']
    list_filter = ['frequency', 'status']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'newsletter']
    list_filter = ['newsletter']
    search_fields = ['subject']

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['newsletter', 'timestamp', 'status']
    list_filter = ['status']
    search_fields = ['newsletter__start_time']