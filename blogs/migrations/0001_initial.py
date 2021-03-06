# Generated by Django 4.0.4 on 2022-06-02 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('category', models.CharField(choices=[('1', 'Frontend'), ('2', 'Backend'), ('3', 'FullStack')], default=('1', 'Frontend'), max_length=50)),
            ],
        ),
    ]
