from django import forms
from .models import Client, Mailing
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'full_name', 'comment']

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))

class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['start_time', 'periodicity', 'status', 'clients']

    def __init__(self, *args, **kwargs):
        super(MailingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['clients'].queryset = Client.objects.all()
        self.fields['clients'].widget.attrs.update({'class': 'selectpicker', 'data-live-search': 'true'})