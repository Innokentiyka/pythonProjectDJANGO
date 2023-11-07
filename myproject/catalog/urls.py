from django.urls import path
from .views import ContactsView, HomeView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, \
    ProductDeleteView, ProductUpdateView, ProductCreateView, ProductListView, VersionDeleteView, VersionUpdateView, \
    VersionCreateView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blogs/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:product_id>/version/add/', VersionCreateView.as_view(), name='version_add'),
    path('version/<int:pk>/update/', VersionUpdateView.as_view(), name='version_update'),
    path('version/<int:pk>/delete/', VersionDeleteView.as_view(), name='version_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

