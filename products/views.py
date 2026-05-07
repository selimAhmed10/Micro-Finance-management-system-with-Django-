from django.shortcuts import render
from django.shortcuts import redirect,get_list_or_404
from django.http import HttpResponse
from .models import Product


def view_all_products(request):
    products=Product.objects.all()
    return render(request,'products/list.html',{'products':products})


