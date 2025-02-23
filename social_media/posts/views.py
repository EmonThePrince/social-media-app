from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from django.db.models import Q
from .models import Post
from .forms import UserRegisterForm

class PostListView(ListView):  # View for listing all posts
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Search functionality
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(content__icontains=search_query) |
                Q(user__username__icontains=search_query)
            )
        
        # Filter by media type
        media_type = self.request.GET.get('media_type')
        if media_type == 'text':
            queryset = queryset.filter(image__exact='')
        elif media_type == 'image':
            queryset = queryset.exclude(image__exact='')
        
        # Filter by specific username
        username_filter = self.request.GET.get('username')
        if username_filter:
            queryset = queryset.filter(user__username__iexact=username_filter)
        
        # Ordering
        ordering = self.request.GET.get('ordering', '-created_at')
        if ordering in ['-created_at', 'created_at']:
            queryset = queryset.order_by(ordering)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add current filter values to context
        context['current_search'] = self.request.GET.get('q', '')
        context['current_media_type'] = self.request.GET.get('media_type', '')
        context['current_username_filter'] = self.request.GET.get('username', '')
        context['current_ordering'] = self.request.GET.get('ordering', '-created_at')
        return context

class PostDetailView(DetailView):  # View for displaying a single post's details
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):  # View for creating a new post
    model = Post
    fields = ['content', 'image']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Post created successfully!')
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # View for updating an existing post
    model = Post
    fields = ['content', 'image']
    
    def form_valid(self, form):
        messages.success(self.request, 'Post updated successfully!')
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # View for deleting a post
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user

def profile(request):  # View for displaying the user's profile and their posts
    posts = Post.objects.filter(user=request.user)
    
    # Filter by media type
    media_type = request.GET.get('media_type')
    if media_type == 'text':
        posts = posts.filter(image__exact='')
    elif media_type == 'image':
        posts = posts.exclude(image__exact='')
    
    # Ordering
    ordering = request.GET.get('ordering', '-created_at')
    if ordering in ['-created_at', 'created_at']:
        posts = posts.order_by(ordering)
    
    context = {
        'posts': posts,
        'current_media_type': media_type or '',
        'current_ordering': ordering
    }
    return render(request, 'posts/profile.html', context)

def register(request):  # View for user registration
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
