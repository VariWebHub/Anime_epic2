# Generated by Django 4.2.2 on 2023-07-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_remove_video_video_video_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='imagen',
            field=models.ImageField(upload_to='imagen_de_blog'),
        ),
    ]