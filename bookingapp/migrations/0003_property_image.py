# Generated by Django 3.2.5 on 2021-07-27 15:05

import cloudinary.models
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0002_gallery_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image',
            field=cloudinary.models.CloudinaryField(default=django.utils.timezone.now, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
