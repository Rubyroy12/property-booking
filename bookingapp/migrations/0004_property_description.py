# Generated by Django 3.2.5 on 2021-07-27 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0003_property_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
