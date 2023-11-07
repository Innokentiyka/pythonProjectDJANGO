from django.views import View
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost, Version
from django.utils.text import slugify
from .models import Product
from .forms import ProductForm, VersionForm


class ContactsView(View):
    template_name = 'main/contacts.html'

    def get(self, request):
        return render(request, self.template_name)


class HomeView(View):
    template_name = 'main/home.html'

    def get(self, request):
        return render(request, self.template_name)





class BlogListView(ListView):
    model = BlogPost
    template_name = 'main/blog_list.html'
    context_object_name = 'blogs'
    queryset = BlogPost.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'main/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class BlogCreateView(CreateView):
    model = BlogPost
    template_name = 'main/blog_create.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = 'main/blog_update.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'main/blog_delete.html'
    success_url = reverse_lazy('blog_list')

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        for product in queryset:
            product.current_version = Version.objects.filter(product=product, is_current=True).first()
        return queryset

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'versions/version_form.html'

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.product.pk})

class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    template_name = 'versions/version_form.html'

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.product.pk})

class VersionDeleteView(DeleteView):
    model = Version
    template_name = 'versions/version_confirm_delete.html'
    context_object_name = 'version'

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.product.pk})