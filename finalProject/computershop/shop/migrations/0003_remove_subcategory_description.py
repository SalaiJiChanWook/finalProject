# Generated by Django 4.2.7 on 2024-01-06 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_ads'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='description',
        ),
    ]
