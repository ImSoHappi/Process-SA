# Generated by Django 3.1.3 on 2020-11-20 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('processAuth', '0001_initial'),
        ('processCore', '0008_flujotareas'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ProblemaTarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='Encabezado problema', max_length=60)),
                ('descripcion', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('responsable', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='processAuth.usermodel')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processCore.task')),
            ],
        ),
    ]
