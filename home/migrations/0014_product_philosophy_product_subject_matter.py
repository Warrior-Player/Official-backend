# Generated by Django 5.0.3 on 2024-04-12 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_style_image_remove_technique_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='philosophy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.philosophy'),
        ),
        migrations.AddField(
            model_name='product',
            name='subject_matter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.subjectmatter'),
        ),
    ]
