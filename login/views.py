from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from my_admin.models import Admin
from officer.models import Officer
from borrower.models import Member

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
    
    if not User.objects.filter(username=username).exists():
        messages.error(request,"The user doesn't exist")
        return redirect('/')
    
    user=authenticate(username=username,password=password)
    
    if User is None:
        messages.error(request,"Invalid authentication")
        return redirect('/')
    
    login(request,user)
    
    if hasattr (user ,'admin'):
        return redirect('/my_admin/dashboard/')
    
    elif hasattr (user ,'Officer'):
        return redirect('/officer/dashboard/')
    
    elif hasattr(user , 'borrower'):
        return redirect('/borrower/dashboard')
    else:
        messages.error(request,"No role assign")
        return redirect('/')
       
    