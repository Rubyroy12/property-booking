# Generated by Django 3.2.5 on 2021-07-28 13:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0014_alter_cart_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='property',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bookingapp.property'),
            preserve_default=False,
        ),
    ]