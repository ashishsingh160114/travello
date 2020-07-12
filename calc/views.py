from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    #return HttpResponse("<h1>HELLO BANKU</h1>")
    #return render(request,'home.html')
    return render(request,'home.html',{'name':'Ashish singh'})


    

def add(request):

    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1 + val2
    return render(request,"result.html",{"result":res})





def mul(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1 * val2
    return render(request,"result.html",{"result":res})