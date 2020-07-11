from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView
)

from blog.models import blog, category
from myprojct.models import projects , Todo

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import User
from .forms import ProfileForm

from .mixins import FieldsMixin, FormValidMixin, FieldsMtodo
# Create your views here.



def dashboard(request):
    SumBlog = blog.objects.count()
    context = {
        'SumBlog' : SumBlog
    }
    return render(request, "panel/index.html", context)

# Profile Usr Update
class Profile(LoginRequiredMixin ,UpdateView):
	model = User
	template_name = "panel/profile.html"
	form_class = ProfileForm
	success_url = reverse_lazy("accounts:profile")

	def get_object(self):
		return User.objects.get(pk = self.request.user.pk)

	def get_form_kwargs(self):
		kwargs = super(Profile, self).get_form_kwargs()
		kwargs.update({
			'user': self.request.user
		})
		return kwargs

# Add Blog In Dashboard
class add_blog(LoginRequiredMixin, FieldsMixin ,FormValidMixin ,CreateView):
    model = blog
    success_url = reverse_lazy("accounts:success-add")
    template_name = "panel/add-blog.html"
# Edit Blog In Dashboard
class edit_blog(LoginRequiredMixin, FieldsMixin ,FormValidMixin ,UpdateView):
    model = blog
    template_name = "panel/edit-blog.html"

class blog_list(LoginRequiredMixin, ListView):
	model = blog
	template_name = "panel/blog-list.html"

# Delete Blog In Dashboard
class del_blog(LoginRequiredMixin ,FormValidMixin ,DeleteView):
    model = blog
    success_url = reverse_lazy("accounts:dashboard")
    template_name = "panel/del-blog.html"
class succsess_add(ListView):
	model = blog
	template_name = "panel/success-add.html"


# ToDo List . add.del.update ...
class todo_list(ListView,FieldsMtodo , CreateView, DeleteView , UpdateView):
	model = Todo
	template_name = "panel/todo-list.html"