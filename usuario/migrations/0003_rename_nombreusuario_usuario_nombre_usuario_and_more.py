# Generated by Django 5.0.4 on 2024-05-21 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_alter_usuario_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='nombreUsuario',
            new_name='nombre_usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tipo',
        ),
    ]
