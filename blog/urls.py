from django.urls import path
from .views import index, b_details, b_list, about, contact

app_name = "blog"

urlpatterns = [
    path('', index.as_view(), name='home'),
    path('blog/', b_list.as_view(), name="bloglist"),
    path('blog/<slug:slug>', b_details.as_view(), name="details"),
    
    path('about/', about, name="about"),
    path('contact', contact, name="contact"),

]