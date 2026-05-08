from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Group
from django.contrib import messages
from officer.models import Officer
from django.contrib.auth.decorators import login_required

@login_required
def view_group(request):
    if not hasattr(request.user, 'admin'):
        return redirect('/')
    groups = Group.objects.all()
    return render(request, 'groups/list.html', {'groups': groups})

def create_group(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        officer_id = request.POST.get('officer')
        
        group = Group.objects.create(
            name=name,
            location=location
        )
        if officer_id:
            officer = get_object_or_404(Officer, id=officer_id)
            group.officer = officer
            group.save()
        
        messages.success(request, "Group created")
        return redirect('/groups/')  
    
    officers = Officer.objects.all()
    return render(request, 'groups/form.html', {'officers': officers})

def modify_group(request, id):
    group = get_object_or_404(Group, id=id)
    
    if request.method == 'POST':
        group.name = request.POST['name']
        group.location = request.POST['location']
        
        officer_id = request.POST.get('officer')
        if officer_id:
            officer = get_object_or_404(Officer, id=officer_id)
            group.officer = officer
        else:
            group.officer = None
        
        group.save()
        messages.success(request, "Group updated successfully")
        return redirect('/groups/')  
    
    officers = Officer.objects.all()
    return render(request, 'groups/form.html', {'group': group, 'officers': officers})

def delete_group(request, id):
    group = get_object_or_404(Group, id=id)
    group.delete()
    messages.success(request, "Group deleted")
    return redirect('/groups/') 