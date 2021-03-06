# Generated by Django 3.1.3 on 2020-11-17 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processAuth', '0001_initial'),
        ('processCore', '0007_tareasubordinada'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlujoTareas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('plazo_maximo', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(0, 'Terminada'), (1, 'En Proceso'), (2, 'Atrasada'), (3, 'Rechazado'), (4, 'Confirmacion')], default=4)),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processCore.process')),
                ('responsables', models.ManyToManyField(to='processAuth.userModel')),
                ('tareas', models.ManyToManyField(to='processCore.Task')),
            ],
        ),
    ]
