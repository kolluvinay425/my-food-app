# Generated by Django 3.0.5 on 2020-05-19 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20200519_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]
