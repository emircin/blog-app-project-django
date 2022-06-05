# Generated by Django 4.0.4 on 2022-06-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/profile_pics/default-profile.png', upload_to='profile_pics'),
        ),
    ]
