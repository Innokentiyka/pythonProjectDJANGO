from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'full_name', 'comment']




User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')  # Добавьте любые другие поля, если требуется