from django.db import models
from django.utils import timezone
from accounts.models import User
# Create your models here.
class cat_prjct(models.Model):
    title = models.CharField(max_length=48, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(unique=True, verbose_name="آدرس دسته بندی")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


STATUS_CHOICES = (
        ('a', "درحال برسی"),
        ('b', "درحال توسعه"),
	    ('d', "آزمایشی"),
		('e', "منتشر شده"),
	)
class projects(models.Model):
    author = models.ForeignKey(User , null=True, on_delete=models.CASCADE, verbose_name="طراح پروژه")
    title = models.CharField(max_length=48, verbose_name="عنوان")
    slug = models.SlugField(unique=True, verbose_name="آدرس پروژه")
    memo = models.TextField(verbose_name="توضیحات")
    category = models.ManyToManyField(cat_prjct, verbose_name="دسته بندی")
    Stime = models.DateTimeField(verbose_name="زمان شروع")
    Etime = models.DateTimeField(verbose_name="زمان پایان")
    price = models.BigIntegerField(verbose_name="قیمت کل")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه ها"


class Todo(models.Model):
    title = models.CharField(max_length=500,  verbose_name='عنوان یادآوری')
    status = models.BooleanField(verbose_name='انجام شده')
    

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "یادآوری"
        verbose_name_plural = "لیست یادآوری ها"