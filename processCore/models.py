from django.db import models
from django.utils import timezone

# Create your models here.

TASK_STATUS = (
    (0, 'Terminada'),
    (1, 'En Proceso'),
    (2, 'Atrasada')
)

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    disabled = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Process(models.Model):
    client = models.ForeignKey('Client', on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    disabled = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Task(models.Model):
    process = models.ForeignKey('Process', on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField()
    status = models.IntegerField(choices = TASK_STATUS, default=1)
    
    def __str__(self):
        return self.name
