from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    interest_rate = models.FloatField()
    total_installment = models.IntegerField()
    per_install_amount = models.FloatField()
    
    def __str__(self):
        return self.name