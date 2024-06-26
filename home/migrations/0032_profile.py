# Generated by Django 5.0.3 on 2024-05-03 22:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_newslettersubscriber_alter_contact_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Profile images')),
                ('full_name', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
