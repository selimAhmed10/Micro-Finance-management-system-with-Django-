from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Borrower(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    age = models.IntegerField()
    nid = models.CharField(max_length=20, unique=True)

    grantor_name = models.CharField(max_length=100)
    grantor_nid = models.CharField(max_length=20)
  
    occupation = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
