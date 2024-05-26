# Generated by Django 5.0.3 on 2024-05-12 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_product_shipping_alter_product_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shipping',
            field=models.CharField(choices=[('free', 'Free'), ('not included', 'Not Included')], default='not included', max_length=40),
        ),
    ]