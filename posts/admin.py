from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "group", "created_at")
    list_filter = ("group", "created_at")
    search_fields = ("message",)


admin.site.register(Post, PostAdmin)