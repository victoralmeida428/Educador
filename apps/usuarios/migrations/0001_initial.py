# Generated by Django 4.2.1 on 2023-05-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=10, unique=True)),
                ('senha', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Neutro'), ('S', 'Prefiro não responder')], max_length=20)),
                ('nascimento', models.DateField()),
            ],
        ),
    ]
