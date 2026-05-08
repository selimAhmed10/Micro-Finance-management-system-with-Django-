from django.db import models
from officer.models import Officer

class Group(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    officer = models.ForeignKey(Officer, on_delete=models.SET_NULL, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name