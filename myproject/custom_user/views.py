from django.core.mail import send_mail
from .forms import UserRegistrationForm
from .token import account_activation_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from .forms import ProductEditForm
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect
from .models import Product
from .forms import ProductForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.is_active = False
            new_user.save()
            subject = 'Activate Your Account'
            message = render_to_string('account_activation_email.html', {
                'user': new_user,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token': account_activation_token.make_token(new_user),
            })
            send_mail(subject, message, 'from@example.com', [new_user.email])
            return redirect('account_activation_sent')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login user here if desired
        return redirect('home')  # Redirect to a success page.
    else:
        return render(request, 'account_activation_invalid.html')

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.user != request.user:
        raise PermissionDenied


@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.user.has_perm('your_app.change_product') or request.user.is_superuser:
        if request.method == 'POST':
            form = ProductEditForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('product_detail', pk=product.pk)
        else:
            form = ProductEditForm(instance=product)
        return render(request, 'product/edit_product.html', {'form': form, 'product': product})
    else:

        return render(request, 'access_denied.html')

def change_product_status(request, pk):
    product = get_object_or_404(Product, pk=pk)


    if request.user.groups.filter(name='Модераторы').exists() or request.user.is_superuser:
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                # Перенаправляем на страницу детального просмотра продукта после сохранения
                return redirect('product_detail', pk=product.pk)
        else:
            form = ProductForm(instance=product)
        return render(request, 'product/edit_product.html', {'form': form})
    else:

        raise PermissionDenied