# Generated by Django 3.0 on 2024-06-07 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=20)),
                ('turno', models.CharField(max_length=5)),
            ],
        ),
    ]
