# Generated by Django 5.0.3 on 2024-04-27 18:47

import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_artist_profileartworkimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(default='artist-image.png', upload_to=home.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='artist',
            name='profileArtworkImage',
            field=models.ImageField(default='Image of your preferred artwork!.png', upload_to=home.models.user_directory_path),
        ),
    ]
