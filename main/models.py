from django.db import models


# Create your models here.
class Slider(models.Model):
    image = models.ImageField(verbose_name="تصویر اسلاید", upload_to="slideImage")
    status = models.BooleanField(default=True, verbose_name="وضعیت نمایش")

    class Meta:
        verbose_name = "اسلاید"
        verbose_name_plural = "اسلاید ها"

