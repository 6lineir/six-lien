from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import blog

# Create your views here.
class index(ListView):
    model = blog
    template_name = "blog/index.html"
class b_list(ListView):
    model = blog
    template_name = "blog/blog.html"

class b_details(DetailView):
    model = blog
    template_name = "blog/details.html"


def about(request):
    return render(request, "blog/about.html")
def contact(request):
    return render(request, "blog/contact.html")