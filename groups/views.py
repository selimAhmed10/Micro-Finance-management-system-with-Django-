from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from .models import Group
from django.contrib import messages
from .models import Officer
from django.contrib.auth.decorators import login_required

@login_required
def view_group(request):
    if not hasattr(request.user,'admin'):
        return redirect('/')
    groups=Group.objects.all()
    return render(request,'groups/list.html',{'groups':groups})



def create_group(request):
    if request.method=='POST':
        Group.objects.create(
        name=request.POST.get['name'],
        location=request.POST.get['location'],
        )
        messages.success(request,"Group created successfull")
        return redirect('view_group')
    return render(request,'groups/form.html')



def modify_group(request,id):
    groups=get_object_or_404(Group,id=id) 
    if request.method=='POST':
        groups.name=request.POST.get['name']
        groups.location=request.POST.get['location']
        groups.save()
        messages.success(request,"GGroup update successfully")
        return redirect('view_group')
    return render(request,'groups/form.html',{'groups':groups})



def delete_group(request,id):
    groups=get_object_or_404(Group,id=id)
    groups.delete()
    messages.success(request,"Group deleted")
    return redirect('view_group')
      
    