from django.db import models

# Create your models here.
class Reg(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    cpassword=models.CharField(max_length=10)
    mobno=models.IntegerField()
    emailid=models.EmailField()