from django.contrib import admin
from django.shortcuts import render

from .models import Client, Mailing, Message, Log, Item
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
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

from django.contrib import admin
from .models import MailingList, Subscription

@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'owner')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'mailing_list', 'is_subscribed', 'subscribed_at')
    list_filter = ('is_subscribed', 'subscribed_at')
    search_fields = ('user__email', 'mailing_list__title')



user = User.objects.get(username='example_user')  # Получаем пользователя
group = Group.objects.get(name='example_group')  # Получаем группу
user.groups.add(group)  # Добавляем пользователя в группу



@permission_required('app_name.permission_codename', raise_exception=True)
def user_list_view(request):
    users = User.objects.all()  # Получаем список всех пользователей
    return render(request, 'myapp/user_list.html', {'users': users})


class MyListView(PermissionRequiredMixin, ListView):
    model = Item
    template_name = 'app_name/item_list.html'
    context_object_name = 'items'
    permission_required = 'app_name.view_item'
