# Generated by Django 3.0.5 on 2020-05-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200403_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/pictures/profilepic.jpg', upload_to='profile_pictures'),
        ),
    ]
