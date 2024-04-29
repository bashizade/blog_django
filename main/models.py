from django.db import models


# Create your models here.
class Slider(models.Model):
    image = models.TextField(verbose_name="تصویر اسلاید")
    status = models.BooleanField(default=True, verbose_name="وضعیت نمایش")


