from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from django.shortcuts import render,redirect
from officer.models import Officer
from borrower.models import Borrower

@login_required
def dashboard(request):
    if not hasattr(request.user,'borrower'):
        return redirect('/')
    total_product=Product.objects.count()
    products=Product.objects.all()
    
    pas = {
        'total_product':total_product,
        'username':request.user.username,
        'password':request.user.password,
        'name':request.user.borrower.name,
        'products':products,
        
    }
    
    return render(request,'borrower/dashboard.html',pas)