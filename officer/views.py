from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from django.shortcuts import render,redirect
from officer.models import Officer
from borrower.models import Borrower

@login_required
def dashboard(request):
    if not hasattr(request.user,'officer'):
        return redirect('/')
    total_product=Product.objects.count()
    products=Product.objects.all()
    pas = {
        'total_product':total_product,
        'username':request.user.username,
        'name':request.user.officer.name,
        'products':products,
        
    }
    
    return render(request,'officer/dashboard.html',pas)