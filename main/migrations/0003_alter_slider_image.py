# Generated by Django 5.0.3 on 2024-04-29 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_slider_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='static/slideImage', verbose_name='تصویر اسلاید'),
        ),
    ]
