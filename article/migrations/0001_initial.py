# Generated by Django 5.0.3 on 2024-04-26 12:06

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('info', models.TextField(verbose_name='خلاصه مطلب')),
                ('description', models.TextField(verbose_name='متن خبر')),
                ('image', models.ImageField(upload_to='article', verbose_name='عکس شاخص')),
                ('hashtags', models.TextField(verbose_name='هشتگ ها')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
            options={
                'verbose_name': 'نوشته',
                'verbose_name_plural': 'نوشته ها',
            },
        ),
    ]
