# Generated by Django 5.0.5 on 2024-05-13 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_alter_shop_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.ImageField(default='/Users/danya/CodeProject/djangoMarketPlace/static/img/catalog/default_product_view.jpeg', upload_to='media/shops/None/'),
        ),
    ]
