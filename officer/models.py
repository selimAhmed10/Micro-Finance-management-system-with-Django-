from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Officer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    officer_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    nid = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    joining_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.officer_id})"