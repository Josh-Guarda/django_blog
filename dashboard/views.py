from django.shortcuts import render

# Create your views here.

def dashboard(request):

    
    context={
        
    }
    return render(request,'dashboard/dashboard.html',context)






def dashboard_posts(request):
    
    
    return render(request,'dashboard/dashboard_posts.html')




def dashboard_categories(request):
    
    
    return render(request,'dashboard/dashboard_categories.html')




def dashboard_users(request):
    
    
    return render(request,'dashboard/dashboard_users.html')



def dashboard_comments(request):
    
    
    
    return render(request,'dashboard/dashboard_comments.html')
    