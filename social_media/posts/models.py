from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):  # Model representing a post in the application
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who created the post
    content = models.TextField()  # Content of the post
    image = models.ImageField(upload_to='posts/', blank=True, null=True)  # Optional image for the post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the post was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the post was last updated

    def __str__(self):  # String representation of the post
        return f"Post by {self.user.username}"

    def get_absolute_url(self):  # Returns the URL to access a specific post
        return reverse('post-detail', kwargs={'pk': self.pk})

    class Meta:  # Meta options for the Post model
        ordering = ['-created_at']  # Order posts by creation date, newest first
