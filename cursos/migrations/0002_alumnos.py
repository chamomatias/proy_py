# Generated by Django 4.2 on 2025-02-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
