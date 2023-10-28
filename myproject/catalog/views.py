from django.views import View
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.utils.text import slugify

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