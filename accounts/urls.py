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
    todo_list,
)


app_name = "accounts"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    #path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    #path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns += [
    path('', dashboard, name="dashboard"),
    path('profile/', Profile.as_view(), name="profile"),
    path('blog-list/', blog_list.as_view(), name="blog-list"),
    path('add-blog/', add_blog.as_view(), name="add-blog"),
    path('edit-blog/<int:pk>', edit_blog.as_view(), name="edit-blog"),
    path('del-blog/<int:pk>', del_blog.as_view(), name="del-blog"),
    path('success-add/', succsess_add.as_view(), name="success-add"),

    path('todo/', todo_list.as_view(), name="todo"),
]