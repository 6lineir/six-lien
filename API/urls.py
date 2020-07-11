from django.contrib import admin
from django.urls import path
from .views import blog_api

urlpatterns = [
    path('v1/', blog_api.as_view(), name='Blog-API'),
]
