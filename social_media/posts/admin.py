from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('content', 'user__username')
    date_hierarchy = 'created_at'
