# Generated by Django 5.1.2 on 2024-10-17 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlumnoT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apaterno', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('amaterno', models.CharField(max_length=50, verbose_name='Apellido Materno')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('fecha_nacimiento', models.DateField(verbose_name='fecha Nacimiento')),
                ('fecha_ingreso', models.DateField(verbose_name='fecha de ingreso')),
            ],
        ),
        migrations.CreateModel(
            name='Frase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(max_length=400, verbose_name='Comentario')),
                ('Alumno_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsecundaria.alumnot')),
            ],
        ),
    ]
