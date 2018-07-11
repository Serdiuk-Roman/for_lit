# from django.shortcuts import render

# from django.views.generic import TemplateView

from post.models import Category, Post

from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from post.serializers import CategorySerializer, PostSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.


class BlogIndex(GenericAPIView):
    template_name = "post/index.html"


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostGenericAPIView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
