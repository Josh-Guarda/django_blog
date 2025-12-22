from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Category
# Create your views here.
def posts_by_category(request,category_id):
    
    #TO AVOID DOING THIS WE UTILIZE CONTEXT PROCESSORS  --> CHECK context_processors.py
    # categories = Category.objects.all()
    posts = Blog.objects.filter(status='Published',category=category_id)
    category = Category.objects.get(id=category_id)
    context={
        # 'categories':categories,
        'category':category,
        'posts':posts,
    }
    return render(request,'post_by_category.html',context)