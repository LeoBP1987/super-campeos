# Generated by Django 5.0.3 on 2024-03-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campeonatos',
            name='publicado',
            field=models.BooleanField(default='True'),
        ),
        migrations.AddField(
            model_name='categorias',
            name='publicado',
            field=models.BooleanField(default='True'),
        ),
        migrations.AddField(
            model_name='times',
            name='publicado',
            field=models.BooleanField(default='True'),
        ),
    ]
