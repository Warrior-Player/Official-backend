# Generated by Django 5.0.3 on 2024-05-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0003_remove_user_hoes_fucked_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('art_enthusiast', 'Art Enthusiast'), ('artist', 'Artist')], default='art_enthusiast', max_length=20),
        ),
    ]
