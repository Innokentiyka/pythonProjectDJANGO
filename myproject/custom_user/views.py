
from .forms import ClientForm
from .models import Client, Newsletter, Message, EmailLog
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
def clients_list(request):
    clients = Client.objects.all()  # Получаем всех клиентов из базы данных
    return render(request, 'clients_list.html', {'clients': clients})



def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients_list')  # Перенаправляем на список клиентов после добавления
    else:
        form = ClientForm()
    return render(request, 'add_client.html', {'form': form})

def edit_client(request, id):
    client = Client.objects.get(pk=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'edit_client.html', {'form': form})



def newsletter_detail(request, id):
    newsletter = Newsletter.objects.get(pk=id)
    return render(request, 'newsletter_detail.html', {'newsletter': newsletter})




def send_newsletter(newsletter_id):
    newsletter = Newsletter.objects.get(pk=newsletter_id)
    clients = Client.objects.all()  # или любой другой способ выбора клиентов
    messages = Message.objects.filter(newsletter=newsletter)

    for message in messages:
        for client in clients:
            try:
                send_mail(
                    subject=message.subject,
                    message=message.body,
                    from_email='ваш_email@gmail.com',
                    recipient_list=[client.email],
                    fail_silently=False,
                )
                log_status = 'Успешно'
            except Exception as e:
                log_status = f'Ошибка: {str(e)}'

            # Логирование отправки сообщения
            EmailLog.objects.create(
                message=message,
                status=log_status,
                response=log_status
            )



User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Не активировать пользователя сразу
            user.save()
            # Отправка письма для верификации
            current_site = get_current_site(request)
            subject = 'Активация вашего аккаунта'
            message = render_to_string('activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('login')  # или страница с информацией о проверке электронной почты
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.email_confirmed = True
        user.save()
        return redirect('login')  # Перенаправление на страницу входа после активации
    else:
        return render(request, 'activation_invalid.html')  # Страница с сообщением об ошибке