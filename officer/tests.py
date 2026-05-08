from django.test import TestCase
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from django.shortcuts import render,redirect
from officer.models import Officer
from borrower.models import Borrower

@login_required
def dashboard(request):
    if not hasattr(request.user,'admin'):
        return redirect('/')
    total_product=Product.objects.count()
    total_borrower=Borrower.objects.count()
    return render(request,'my_admin/dashboard.html',total_product,total_borrower)