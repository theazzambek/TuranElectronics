# Generated by Django 5.0.4 on 2024-04-21 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_brand_allmodels'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='allmodels',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='all_brand', to='shop.allmodels'),
        ),
    ]
