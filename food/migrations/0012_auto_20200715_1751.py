# Generated by Django 3.0.5 on 2020-07-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_auto_20200524_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(max_length=300),
        ),
    ]