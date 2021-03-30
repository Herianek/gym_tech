from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jidelnicek(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jidelnicek",null=True)
    name = models.CharField(max_length=200)

    def __str__(self): #rozšifruje str
        return self.name


class Jidla(models.Model):
    jidelnicek = models.ForeignKey(Jidelnicek, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self): #rozšifruje str
        return self.text
