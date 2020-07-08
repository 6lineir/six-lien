from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    dashboard, 
    Profile, 
    add_blog,
    edit_blog,  
    blog_list, 
    del_blog,
    succsess_add,
)


app_name = "accounts"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns += [
    path('', dashboard, name="dashboard"),
    path('profile/', Profile.as_view(), name="profile"),
    path('blog-list/', blog_list.as_view(), name="blog-list"),
    path('add-blog/', add_blog.as_view(), name="add-blog"),
    path('edit-blog/<int:pk>', edit_blog.as_view(), name="edit-blog"),
    path('del-blog/<int:pk>', del_blog.as_view(), name="del-blog"),
    path('success-add/', succsess_add.as_view(), name="success-add"),

]