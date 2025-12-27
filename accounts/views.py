from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .forms import CreateUserForm

def register(request):
    hide_nav=True
    hide_category=True
    hide_footer=True
    
    
    form = CreateUserForm()
    
    # print(form)
    
    
    
    
    context={
        'hide_nav':hide_nav,
        'hide_category':hide_category,
        'hide_footer':hide_footer,
        'form':form
    }
    return render(request,'auth_template/register.html',context)
