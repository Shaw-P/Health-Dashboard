from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    birth = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    repassword = models.CharField(max_length=30)
    height = models.IntegerField()
    weight = models.IntegerField()
    neck_line = models.IntegerField()
    ess = models.IntegerField()