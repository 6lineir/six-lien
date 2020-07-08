from django.contrib import admin
from .models import category, blog
# Register your models here.
admin.site.site_header = "داشبورد مدیریت وب اپلیکیشن"

class adminblog(admin.ModelAdmin):
    list_display = (
        "title", 
        "photo_tag",     
        "publish",
        "status",
        "author",
    )
    list_filter = ("publish", "status",)

admin.site.register(category)
admin.site.register(blog, adminblog)