from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'view_count')
    list_filter = ('publication_date',)
    search_fields = ('title', 'content',)