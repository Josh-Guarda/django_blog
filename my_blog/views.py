from django.shortcuts import render,redirect
from blogs.models import Category,Blog,About,Socials
from django.contrib.auth.models import User
from django.http import HttpResponse
 
def home(request):
    categories = Category.objects.all()  # THIS IS OPTIONAL TO DECLARE SINCE WE ALREADY HAVE THE CONTEXT PROCESSOR for the categories
    featured_post = Blog.objects.filter(is_featured = True, status='Published').order_by('-updated_at')
    un_featured_post = Blog.objects.filter(is_featured = False, status='Published').order_by('-updated_at')
    
    # print(User._meta.get_fields())# Command to get all fields from User or other predefined Models
    try:
        about = About.objects.get()
        socials =Socials.objects.all()
    except:
        about = None
        socials= None
    context = {
        'categories':categories, # THIS IS OPTIONAL TO DECLARE SINCE WE ALREADY HAVE THE CONTEXT PROCESSOR for the categories
        'featured_post':featured_post,
        'un_featured_post':un_featured_post,
        'about':about,
        'socials':socials
        
    }
    return render(request,'home.html',context)








    
    
    
