# Generated by Django 5.0.3 on 2024-04-07 03:06

import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_artist_city_alter_product_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='biography',
            field=models.TextField(default="Born in xxxx, at 'city', I was always eager to paint....", max_length=300),
        ),
        migrations.AddField(
            model_name='artist',
            name='profileArtworkImage',
            field=models.ImageField(default='artwork image to be shown in your profile', upload_to=home.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='artist',
            name='description',
            field=models.TextField(default='With an unwavering passion for art, this dedicated enthusiasm aspires to illuminate and enrich the lives of others through the captivating power of creativity...', max_length=300),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(default='artist image', upload_to=home.models.user_directory_path),
        ),
    ]