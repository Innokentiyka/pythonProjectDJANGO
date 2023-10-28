from django.urls import path
from .views import ContactsView, HomeView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blogs/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)