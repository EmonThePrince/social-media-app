from django.contrib import admin  # Admin site for managing the application
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  # URL patterns for the application
    path('admin/', admin.site.urls),  # Admin interface URL
    path('', include('posts.urls')),  # Include URLs from the posts app
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Login URL
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),  # Logout URL
]

if settings.DEBUG:  # Serve media files only in debug mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
