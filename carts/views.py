from django.shortcuts import render
from .import views
# Create your views here.
def carts(request):
    return render(request,'store/cart.html')