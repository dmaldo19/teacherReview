# Generated by Django 5.0.4 on 2024-04-27 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('departamento', models.CharField(max_length=50)),
            ],
        ),
    ]
