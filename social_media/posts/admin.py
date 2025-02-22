from django.contrib import admin
from .models import Post  # Importing the Post model for admin management

@admin.register(Post)  # Registering the Post model with the admin site
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')  # Fields to display in the admin list view
    list_filter = ('created_at', 'user')  # Filters for the admin list view
    search_fields = ('content', 'user__username')  # Fields to search in the admin interface
    date_hierarchy = 'created_at'  # Date hierarchy for filtering by creation date
