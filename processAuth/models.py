from django.db import models
from django.contrib.auth.models import User

# Create your models here.

USER_ROLE = (  
    (0,'Administrador'),
    (1,'Funcionario'),
    (2,'Diseñador')
)

class userModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.IntegerField(choices = USER_ROLE)
    created_at = models.DateTimeField(auto_now_add=True)
    disabled = models.BooleanField(default = False)

    def __str__(self):
        return self.name

