from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostListCreateAPIView(generics.ListCreateAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializer
  

class BlogPostRetrieveUpdateDstroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializer