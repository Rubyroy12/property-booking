# Generated by Django 3.2.5 on 2021-07-27 14:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='property',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='bookingapp.property'),
            preserve_default=False,
        ),
    ]
