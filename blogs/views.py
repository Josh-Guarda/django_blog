from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Blog,Category

#Advance multiple search using multiple condition or operator using Q
from django.db.models import Q


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



def blogs(request,slug):
    single_post = get_object_or_404(Blog,slug=slug,status='Published')
    # print(single_post)
    context={
        'single_post':single_post
    }
    return render (request,'blogs.html',context)


def search(request):
    keyword=request.GET.get('keyword')
    search_post = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword)| Q(author__first_name__icontains=keyword),status='Published') # The ouput here is a QuerySet e.g <QuerySet [<Blog: This is My first Blog>]> the way to iterate with it is using forloop on the template or in this function check the loop below. 
    
    #Or operator for additional search condition
    
    # print(search_post)
    # for post in search_post:
    #     print(post)
    context={
        'search_post':search_post,
        'keyword':keyword
    }
    return render(request,'search.html',context)