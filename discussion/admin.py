from django.contrib import admin
from .models import Post, Reply


class RepliesInline(admin.StackedInline):
    model = Reply
    can_delete = True
    verbose_name_plural = "replies"


class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = ((RepliesInline,))


admin.site.register(Post, PostAdmin)
