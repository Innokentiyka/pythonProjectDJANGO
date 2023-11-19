from django.shortcuts import render, get_object_or_404, redirect
from myproject.custom_user.forms import ProductForm
from myproject.custom_user.models import Product


# Представление для списка продуктов
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/list.html', {'products': products})

# Представление для детального просмотра продукта
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/detail.html', {'product': product})

# Представление для создания нового продукта
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product/form.html', {'form': form})

# Представление для редактирования продукта
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/form.html', {'form': form})

# Представление для удаления продукта
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product/confirm_delete.html', {'product': product})