# Generated by Django 5.0.5 on 2024-05-13 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_review_reviews_count_alter_shop_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='key_features',
            field=models.TextField(db_default='', default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(db_default='', default=''),
        ),
    ]
