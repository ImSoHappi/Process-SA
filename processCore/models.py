from django.db import models
from django.utils import timezone

# Create your models here.

TASK_STATUS = (
    (0, 'Terminada'),
    (1, 'En Proceso'),
    (2, 'Atrasada'),
    (3, 'Rechazado'),
    (4, 'Confirmacion')
)

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    disabled = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class UnidadInterna(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey('Client', on_delete = models.CASCADE)
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
    responsable = models.ForeignKey('processAuth.userModel', on_delete = models.CASCADE, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField()
    status = models.IntegerField(choices = TASK_STATUS, default=4)
    
    def __str__(self):
        return self.name

class TareaSubordinada(models.Model):
    task = models.ForeignKey('Task', on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    responsable = models.ForeignKey('processAuth.userModel', on_delete = models.CASCADE, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField()
    status = models.IntegerField(choices = TASK_STATUS, default=4)
    
    def __str__(self):
        return self.name

class Rejectcomment(models.Model):
    task = models.ForeignKey('Task', on_delete = models.CASCADE)
    responsable = models.ForeignKey('processAuth.userModel', on_delete = models.CASCADE, blank=True)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.reason