from django.contrib import admin
from .models import Client, Mailing, Message, Log

class MessageInline(admin.StackedInline):
    model = Message
    extra = 1  # Количество форм для новых сообщений

class LogInline(admin.TabularInline):
    model = Log
    extra = 0  # Не добавлять пустые формы для новых логов

class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'comment')
    search_fields = ('full_name', 'email')

class MailingAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'periodicity', 'status')
    list_filter = ('periodicity', 'status')
    inlines = [MessageInline]
    filter_horizontal = ('clients',)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'mailing')
    inlines = [LogInline]

class LogAdmin(admin.ModelAdmin):
    list_display = ('message', 'attempt_time', 'status')
    list_filter = ('status',)
    search_fields = ('message__subject',)

admin.site.register(Client, ClientAdmin)
admin.site.register(Mailing, MailingAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Log, LogAdmin)