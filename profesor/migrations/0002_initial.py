# Generated by Django 5.0.4 on 2024-04-27 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materia', '0002_initial'),
        ('profesor', '0001_initial'),
        ('publicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='materias',
            field=models.ManyToManyField(through='publicacion.Publicacion', to='materia.materia'),
        ),
    ]
