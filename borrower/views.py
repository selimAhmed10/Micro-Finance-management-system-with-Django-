from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Borrower
from groups.models import Group
from products.models import Product
from borrower.models import Borrower

@login_required
def dashboard(request):
    if not hasattr(request.user,'borrower'):
        return redirect('/')
    
    borrower = request.user.borrower
    products = Product.objects.all()
    
    context = {
        'username': request.user.username,
        'name': borrower.name,
        'products': products,
    }
    return render(request, 'borrower/dashboard.html', context)








@login_required
def group_members(request, group_id):
    if not hasattr(request.user, 'officer'):
        return redirect('/')
    
    group = get_object_or_404(Group, id=group_id, officer=request.user.officer)
    borrowers = Borrower.objects.filter(group=group)
    
    return render(request, 'borrower/list.html', {
        'group': group,
        'borrowers': borrowers,
    })


@login_required
def borrower_list(request):
    if not hasattr(request.user, 'officer'):
        return redirect('/')
    borrowers = Borrower.objects.all()
    return render(request, 'borrower/all_list.html', {'borrowers': borrowers})

@login_required
def add_member(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect(f'/borrower/add/{group_id}/')
        
        user = User.objects.create_user(username=username, password=password)
        
        Borrower.objects.create(
            user=user,
            name=request.POST['name'],
            fathers_name=request.POST['fathers_name'],
            mothers_name=request.POST['mothers_name'],
            age=request.POST['age'],
            nid=request.POST['nid'],
            grantor_name=request.POST['grantor_name'],
            grantor_nid=request.POST['grantor_nid'],
            occupation=request.POST['occupation'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            group=group
        )
        
        messages.success(request, f"Member '{username}' added!")
        return redirect(f'/borrower/members/{group_id}/')
    
    return render(request, 'borrower/form.html', {
        'borrower': None,
        'group': group,
    })

@login_required
def edit_member(request, id):
    borrower = get_object_or_404(Borrower, id=id)
    group_id = borrower.group.id
    
    if request.method == 'POST':
        borrower.name = request.POST['name']
        borrower.fathers_name = request.POST['fathers_name']
        borrower.mothers_name = request.POST['mothers_name']
        borrower.age = request.POST['age']
        borrower.nid = request.POST['nid']
        borrower.grantor_name = request.POST['grantor_name']
        borrower.grantor_nid = request.POST['grantor_nid']
        borrower.occupation = request.POST['occupation']
        borrower.phone = request.POST['phone']
        borrower.address = request.POST['address']
        borrower.save()
        
        messages.success(request, "Member updated!")
        return redirect(f'/borrower/members/{group_id}/')
    
    return render(request, 'borrower/form.html', {
        'borrower': borrower,
        'group': borrower.group,
    })

@login_required
def delete_member(request, id):
    member = get_object_or_404(Borrower, id=id)
    group_id = member.group.id
    username = member.user.username
    member.user.delete()
    
    messages.success(request, f"Member '{username}' deleted!")
    return redirect(f'/borrower/members/{group_id}/')