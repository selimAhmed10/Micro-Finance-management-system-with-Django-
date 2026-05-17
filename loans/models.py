from django.db import models
from django.contrib.auth.models import User
from borrower.models import Borrower
from groups.models import Group
from products.models import Product

class Loan(models.Model):
    Status=(
        ('pending','Pending'),
        ('approved','Aproved'),
        ('rejected','Rejected'),
    )
    
    borrower=models.ForeignKey(Borrower,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    group=models.ForeignKey(Group,on_delete=models.CASCADE)
    amount=models.FloatField()
    interest_rate=models.FloatField()
    total_installment=models.FloatField()
    per_install_amount=models.FloatField()
    status=models.CharField(max_length=10,choices=Status,default='pending')
    
    def __str__(self):
        return self.borrower()
    


