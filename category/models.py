from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
