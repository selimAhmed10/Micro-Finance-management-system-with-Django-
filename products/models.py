from django.db import models

# Create your models here.
class Product(models.Model):
    
    name=models.CharField(max_length=50)
    amount=models.DecimalField(max_digits=5,decimal_places=2)
    interest_rate=models.DecimalField(max_digits=2,decimal_places=2)
    total_installment=models.IntegerField()
    per_install_amount=models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return self.name