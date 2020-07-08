from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	phone = models.CharField(max_length=12, blank=True, verbose_name="شماره تماس")
	id_telegram = models.URLField(default="https://t.me/", verbose_name="تلگرام ID")
	id_instagram = models.URLField(default="https://instagram.com/", verbose_name="اینستاگرام ID")
	github = models.URLField(default="https://github.com/", verbose_name="گیت هاب")
	avatar = models.ImageField(upload_to='avatar', blank=True, verbose_name="آواتار")
	is_author = models.BooleanField(default=False, verbose_name="وضعیت نویسندگی")
	special_user = models.DateTimeField(default=timezone.now, verbose_name="کاربر ویژه تا")

	def is_special_user(self):
		if self.special_user > timezone.now():
			return True
		else:
			return False
	is_special_user.boolean = True
	is_special_user.short_description = "وضعیت کاربر ویژه"