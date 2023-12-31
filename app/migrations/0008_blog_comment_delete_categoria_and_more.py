# Generated by Django 4.2.2 on 2023-07-03 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_categoria_imagenblog_publicacion_etiqueta_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='blog_images')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.blog')),
            ],
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='publicacion',
        ),
        migrations.RemoveField(
            model_name='etiqueta',
            name='publicaciones',
        ),
        migrations.DeleteModel(
            name='ImagenBlog',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
        migrations.DeleteModel(
            name='Etiqueta',
        ),
        migrations.DeleteModel(
            name='Publicacion',
        ),
    ]
