# Generated by Django 4.2.2 on 2023-07-01 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_heroitem_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='trendingproduct',
            table='tb_trending',
        ),
    ]
