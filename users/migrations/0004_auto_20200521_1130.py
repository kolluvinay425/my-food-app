# Generated by Django 3.0.5 on 2020-05-21 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200521_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/pictures/profilepic.jpg', upload_to='media/profile_pictures'),
        ),
    ]
