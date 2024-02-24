from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Mailing
from .forms import ClientForm, MailingForm


# Клиенты
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('client_list')

# Рассылки
def mailing_list(request):
    mailings = Mailing.objects.all()
    return render(request, 'mailing_list.html', {'mailings': mailings})

def mailing_create(request):
    if request.method == 'POST':
        form = MailingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mailing_list')
    else:
        form = MailingForm()
    return render(request, 'mailing_form.html', {'form': form})

def mailing_edit(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    if request.method == 'POST':
        form = MailingForm(request.POST, instance=mailing)
        if form.is_valid():
            form.save()
            return redirect('mailing_list')
    else:
        form = MailingForm(instance=mailing)
    return render(request, 'mailing_form.html', {'form': form})

def mailing_delete(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    mailing.delete()
    return redirect('mailing_list')

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_newsletter_email(user_email):
    subject = "Welcome to Our Newsletter"
    content = "Here is the body of your email..."
    unsubscribe_link = "http://example.com/unsubscribe"

    message = render_to_string('email_template.html', {
        'subject': subject,
        'content': content,
        'unsubscribe_link': unsubscribe_link,
    })

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
        html_message=message,  # Указываем, что сообщение в формате HTML
    )

