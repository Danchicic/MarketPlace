# Generated by Django 5.0.5 on 2024-05-12 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='orders_complete',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='products',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='reviews_count',
        ),
    ]