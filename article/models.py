from django.utils import timezone

from django.db import models
from category.models import Category


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    info = models.TextField(verbose_name="خلاصه مطلب")
    description = models.TextField(verbose_name="متن خبر")
    image = models.ImageField(upload_to="article", verbose_name="عکس شاخص")
    hashtags = models.TextField(verbose_name="هشتگ ها")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "نوشته"
        verbose_name_plural = "نوشته ها"
