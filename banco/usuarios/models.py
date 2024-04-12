from django.db import models

# Create your models here.

class Usuario(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length= 50)

    def __str__(self):
        return self.name