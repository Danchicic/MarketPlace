# Generated by Django 5.0.5 on 2024-06-08 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_cart_cart_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='date_create',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
