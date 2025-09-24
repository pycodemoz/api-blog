from django.urls import path
from .views import BlogPostListCreateAPIView, BlogPostRetrieveUpdateDstroyAPIView



urlpatterns = [
  
  path('blog/api/v1/', BlogPostListCreateAPIView.as_view(), name='blog-create-api-view' ),
  
  path('blog/api/v1/<int:pk>/', BlogPostRetrieveUpdateDstroyAPIView.as_view(), name='blog-detail-api-view'),
  
]