from django.shortcuts import render
from shoppapp.models import Product
from django.db.models.query import Q
# Create your views here.
def searchdetails(request):
    products=None
    query=None
    if 's' in request.GET:
        query=request.GET.get('s')
        products=Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))


    return render(request,"search.html" , {'products':products,'query':query})
