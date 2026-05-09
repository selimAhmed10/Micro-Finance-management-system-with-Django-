from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from django.shortcuts import render, redirect, get_object_or_404
from officer.models import Officer
from borrower.models import Borrower
from django.contrib.auth.models import User

@login_required
def dashboard(request):
    if not hasattr(request.user, 'officer'):
        return redirect('/')
    total_product = Product.objects.count()
    products = Product.objects.all()
    pas = {
        'total_product': total_product,
        'username': request.user.username,
        'name': request.user.officer.name,
        'products': products,
    }
    return render(request, 'officer/dashboard.html', pas)


@login_required
def view_officer(request):
    if not hasattr(request.user, 'admin'):
        return redirect('/')
    officers = Officer.objects.all()
    return render(request, 'officer/list.html', {'officers': officers})


def create_officer(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('/officer/create/')
        
        user = User.objects.create_user(
            username=username,
            password=password
        )
        
        officer = Officer.objects.create(
            user=user,
            officer_id=request.POST['officer_id'],
            name=request.POST['name'],
            nid=request.POST['nid'],
            phone=request.POST['phone'],
            address=request.POST['address'],
        )
        messages.success(request, "Officer created successfully")
        return redirect('/officer/view/')
    
    return render(request, 'officer/form.html')


def modify_officer(request, id):
    officer = get_object_or_404(Officer, id=id)
    if request.method == 'POST':
        officer.officer_id = request.POST['officer_id']
        officer.name = request.POST['name']
        officer.nid = request.POST['nid']
        officer.phone = request.POST['phone']
        officer.address = request.POST['address']
        officer.save()
        messages.success(request, "Officer updated successfully")
        return redirect('/officer/view/')
    
    return render(request, 'officer/form.html', {'officer': officer})

def delete_officer(request, id):
    officer = get_object_or_404(Officer, id=id)
    username = officer.user.username
    officer.user.delete()
    messages.success(request,"Officer deleted successfully")
    return redirect('/officer/view/')