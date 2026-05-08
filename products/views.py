from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Product


def view_all_products(request):
    product=Product.objects.all()
    return render(request,'products/list.html',{'product':product})

def create_product(request):
    if request.method=='POST':
        Product.objects.create(
            name=request.POST['name'],
            amount=request.POST['amount'],
            interest_rate=request.POST['interest_rate'],
            total_installment=request.POST['total_installment'],
            per_install_amount=request.POST['per_install_amount']  
        )
        
        return redirect('view_all_products')
    return render (request,'products/form.html')

def update_product(request,id):
    product=get_object_or_404(Product,id=id)
    if request.method=='POST':
        product.name=request.POST['name']
        product.amount=request.POST['amount']
        product.interest_rate=request.POST['interest_rate']
        product.total_installment=request.POST['total_installment']
        product.per_install_amount=request.POST['per_install_amount']  
        product.save()
        return redirect('view_all_products')
    return render(request,'products/form.html',{'product':product})

def delete_product(request,id):
    product=get_object_or_404(Product,id=id)
    product.delete()
    return redirect('view_all_products')
        


