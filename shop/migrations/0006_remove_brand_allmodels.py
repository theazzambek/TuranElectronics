# Generated by Django 5.0.4 on 2024-04-21 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_brand_allmodels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='allmodels',
        ),
    ]
