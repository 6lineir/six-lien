from django.db import models
from accounts.models import User
from django.utils.html import format_html
from django.utils import timezone

# Create your models here.

class category(models.Model):
    cat_title = models.CharField(max_length=48, verbose_name='دسته بندی')
    cat_slug = models.SlugField(verbose_name='لینک دسته بندی') 
    
    def __str__(self):
        return self.cat_title
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"



STATUS_CHOICES = (
        ('v', "ویژه"),
        ('f', "پیش نویس"),
	    ('d', "درانتظار تایید"),
		('p', "منتشر شده"),
	)
class blog(models.Model):
    author = models.ForeignKey(User , null=True, on_delete=models.CASCADE, verbose_name="نویسنده")
    title = models.CharField(max_length=48, verbose_name='عنوان' )
    slug = models.SlugField(unique=True, verbose_name='لینک نوشته')
    bmemo = models.TextField(verbose_name='متن بلاگ')
    photo = models.ImageField(upload_to='pic-blog', verbose_name='تصویر بلاگ')
    category = models.ManyToManyField(category, verbose_name='دسته بندی')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "وبلاگ"
        verbose_name_plural = "بلاگ ها"
    
    def photo_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.photo.url))
    photo_tag.short_description = "تصویر"	

