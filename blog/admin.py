from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'preview',
                    'date_created', 'is_published', 'views_count', )
    list_filter = ('is_published', )
    search_fields = ('title', 'content', )
