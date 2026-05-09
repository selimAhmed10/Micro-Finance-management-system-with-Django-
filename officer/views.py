from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from django.shortcuts import render,redirect,get_object_or_404
from officer.models import Officer
from borrower.models import Borrower
from django.contrib.auth.models import User

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


@login_required
def view_officer(request):
    if not hasattr(request.user,'admin'):
        return redirect('/')
    officer=Officer.objects.all()
    return render(request,'officer/list.html',{'officer':officer})


def create_officer(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POSt['password']
        
        if Officer.objects.filter(username=username).exists():
            messages.error(request,"Username already have in officer")
            return redirect('create_officer')
        
        user=User.objects.create(
            username=username,
            password=password
        )
        
        officer=Officer.objects.create(
            user=user,
            officer_id=request.POST['officer_id']
            name=request.POST['name']
            nid=request.POST['nid']
            phone=request.POST['phone'] 
            address=request.POST['address']           
            
        )
        messages.success(request,"Officer created")
        return redirect('view_oficcer')
    return render(request,'officer/form.html')

def modify_officer(request,id):
    officer=get_object_or_404(Officer,id=id)
    if request.method=='POST':
        officer.officer_id=request.POST['officer_id']
        officer.name=request.POST['name']
        officer.nid=request.POST['nid']
        officer.phone=request.POST['phone']
        officer.address=request.POST['location']
        
        officer.save()
        messages.success(request,"Modify successfull")
        return redirect('view_officer')
    return redirect(request,'officer/form.html',{'officer':officer})

def delete_officer(request,id):
    officer=get_object_or_404(Officer,id=id)
    officer.delete()
    messages("Successfully delete the officer ")
    return redirect('view_officer')
