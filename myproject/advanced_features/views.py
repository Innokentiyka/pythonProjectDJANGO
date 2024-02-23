from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseForbidden
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse


User = get_user_model()

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        self.send_verification_email(user)
        return redirect(self.get_success_url())

    def send_verification_email(self, user):
        subject = "Account Activation Required"
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': 'your_domain.com',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        user.email_user(subject, message)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.email_verified = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return HttpResponse('Activation link is invalid!')

class CustomLoginView(LoginView):
    template_name = 'login.html'


class CustomUser(AbstractUser):
    is_blocked = models.BooleanField(default=False)

class Mailing(models.Model):
    # Ваши другие поля модели
    is_active = models.BooleanField(default=True)

def toggle_mailing_active(request, mailing_id):
    if not request.user.has_perm('yourapp.change_mailing'):
        # Проверьте, что пользователь имеет права на изменение рассылок
        return HttpResponseForbidden()

    mailing = get_object_or_404(Mailing, id=mailing_id)
    mailing.is_active = not mailing.is_active
    mailing.save()

    return redirect(reverse('mailings_list'))

