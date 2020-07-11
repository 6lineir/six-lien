from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.
from blog.models import blog
from .serializers import BlogSerializer

class blog_api(generics.ListAPIView):
    queryset = blog.objects.all()
    serializer_class = BlogSerializer