# Generated by Django 4.0.4 on 2022-06-06 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModeloFamilia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=30)),
                ('descripcion', models.CharField(default='Esta es una descripcion corta de un familiar', max_length=100)),
                ('edad', models.IntegerField()),
                ('fdn', models.DateField()),
                ('parentesco', models.CharField(max_length=20)),
            ],
        ),
    ]
