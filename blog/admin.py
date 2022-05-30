from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    To use the summernote in the content field (blog content),
    Display title, slug, status, and date created on admin panel,
    Add a search field on admin panel from the title and content fields
    """
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Docstring
    """
    list_filter = ('approved', 'created_on')
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    search_fields = ['name', 'email', 'body']
    actions = ['approved_commets']

    def approved_comments(self, request, queryset):
        """
        To approve any comments on the blog
        to update models
        """
        queryset.update(approved="True")
