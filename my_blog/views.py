from django.shortcuts import render,redirect
from django.http import HttpResponse as shortcut



def home(request):
    
    return render(request,'home.html')
    