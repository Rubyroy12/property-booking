# Generated by Django 3.2.5 on 2021-07-28 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0009_alter_cart_payment_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='payment_mode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookingapp.paymentmode'),
        ),
    ]
