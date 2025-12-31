from django.shortcuts import render

# Create your views here.

def dashboard(request):
    hide_nav=True
    hide_category=True
    hide_footer=True
    
    
    context={
        'hide_nav':hide_nav,
        'hide_category':hide_category,
        'hide_footer':hide_footer,
    }
    return render(request,'dashboard/dashboard.html',context)