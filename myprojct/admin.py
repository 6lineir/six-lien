from django.contrib import admin
from .models import projects, cat_prjct, Todo
# Register your models here.

class PrjctAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "Stime",
        "Etime",
        "status",
    )
    list_filter = ("status","Stime","Etime",)

admin.site.register(Todo)
admin.site.register(projects, PrjctAdmin)
admin.site.register(cat_prjct)
