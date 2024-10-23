#views.py
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

def application_post_view(request, company_name):
    print(f"Received request for company: {company_name}")

    # Fetch posts based on the company_name
    posts = Post.objects.filter(company_name=company_name)

    # Serialize posts to JSON using the serializer
    data = PostSerializer(posts, many=True, context={'request': request}).data  # Using the serializer to handle serialization

    return JsonResponse(data, safe=False)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

