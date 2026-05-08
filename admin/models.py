from django.db import models
from django.contrib.auth.models import User


class Admin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    phone_num=models.CharField(max_length=14)
    degisnation=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    