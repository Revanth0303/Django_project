from django.shortcuts import render
from .models import Offers
# Create your views here.
def index(request):

    offs=Offers.objects.all()
    return render(request,'index.html',{'offs':offs})