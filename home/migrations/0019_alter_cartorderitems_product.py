# Generated by Django 5.0.3 on 2024-04-26 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_cartorderitems_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorderitems',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.product'),
        ),
    ]
