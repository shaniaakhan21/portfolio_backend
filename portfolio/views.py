# your_app/views.py
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

# This function handles rendering a specific post for a company
def application_post_view(request, company_name):
    post = get_object_or_404(Post, company_name=company_name)
    return render(request, 'application_post.html', {'post': post})

# This class-based view handles API requests for posts
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
