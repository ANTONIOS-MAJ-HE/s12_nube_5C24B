# Generated by Django 4.2.7 on 2023-11-20 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='fotos/')),
            ],
        ),
    ]