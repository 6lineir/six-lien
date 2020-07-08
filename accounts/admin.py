from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


UserAdmin.fieldsets[2][1]['fields'] = (
										'phone',
										'id_telegram',
										'id_instagram',
										'github',
										'avatar',
										'is_active', 
										'is_staff', 
										'is_superuser', 
										'is_author', 
										'special_user', 
										'groups', 
										'user_permissions'
									)
UserAdmin.list_display += ('is_author', 'is_special_user', 'phone')

admin.site.register(User, UserAdmin)