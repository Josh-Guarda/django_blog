from django.shortcuts import render,redirect
from blogs.models import Category,Blog
from django.contrib.auth.models import User
 
def home(request):
    categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured = True, status='Published').order_by('-updated_at')
    un_featured_post = Blog.objects.filter(is_featured = False, status='Published').order_by('-updated_at')
    
    print(User._meta.get_fields())# Command to get all fields from User or other predefined Models
    context = {
        'categories':categories,
        'featured_post':featured_post,
        'un_featured_post':un_featured_post
        
    }
    return render(request,'home.html',context)
    
    