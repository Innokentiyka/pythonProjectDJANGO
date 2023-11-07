from django import forms
from django.core.exceptions import ValidationError
from .models import Product, Version

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def clean_name(self):
        name = self.cleaned_data['name']
        if any(forbidden_word in name for forbidden_word in FORBIDDEN_WORDS):
            raise ValidationError("Название продукта содержит запрещённые слова.")
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        if any(forbidden_word in description for forbidden_word in FORBIDDEN_WORDS):
            raise ValidationError("Описание продукта содержит запрещённые слова.")
        return description
class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_title', 'is_current']