# Generated by Django 5.0.3 on 2024-05-08 17:36

import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_cartorder_address_cartorder_city_cartorder_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='oid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='123456789', length=10, max_length=30, prefix='', unique=True),
        ),
        migrations.AddField(
            model_name='cartorder',
            name='zip',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
