from django.shortcuts import render
from django.shortcuts import get_object_or_404
from blogs.models import Blog

# Create your views here.

def dashboard(request):
    context={
        
    }
    return render(request,'dashboard/dashboard.html',context)




def dashboard_posts(request):
    Posts = Blog.objects.all()
    # print(Post)
    context={
        'posts':Posts
    }
    
    return render(request,'dashboard/dashboard_posts.html',context)



def PostDetails(request,id):
    post = get_object_or_404(Blog,id=id)
    
    context={
        'post':post
    }
    
    return render(request,'dashboard/dashboard_posts_detail.html',context)
    









































def dashboard_categories(request):
    
    
    return render(request,'dashboard/dashboard_categories.html')




def dashboard_users(request):
    
    
    return render(request,'dashboard/dashboard_users.html')



def dashboard_comments(request):
    
    
    
    return render(request,'dashboard/dashboard_comments.html')
    