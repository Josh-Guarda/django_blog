from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from blogs.models import Blog

#using core django generic views

from django.views.generic import TemplateView,View,ListView,DetailView
from django.core import serializers
from django.http import JsonResponse



# Create your views here.

def dashboard(request):
    return render(request,'dashboard/dashboard.html')



# FunctionBase View
# def dashboard_posts(request):
#     Posts = Blog.objects.all()
#     # print(Post)
#     context={
#         'posts':Posts
#     }
#     return render(request,'dashboard/dashboard_posts.html',context)


#ClassBase View using generic in core django NOTE: Follow the format below
class PostView(ListView):
    template_name = 'dashboard/dashboard_posts.html'  # Template that we will call
    context_object_name = 'posts' # This refers on the Loop object that we loop in our template
    
    #This is the function that will run the Query Set
    def get_queryset(self):
        Posts = Blog.objects.all()
        # print(Posts)
        return Posts


#DISPLAY DATA ON A SEPARATE PAGE
#Temporary commented this since my Target is to pass the data-id to a modal 
#Note: that this PosDetailView is correct if we are dealing with a separate template
# class PostDetailView(DetailView):
#     model = Blog
#     template_name = 'dashboard/dashboard_posts_detail.html'
    
    
def get_data(request,pk):
    qs = Blog.objects.filter(pk=pk)
    if request.method =='GET':
        data = serializers.serialize('json',qs)
        # print(data)
        return JsonResponse({'data':data},safe=False)
    

def get_edit_data(request,pk):
    qs = Blog.objects.filter(pk=pk)
    if request.method =='GET':
        data = serializers.serialize('json',qs)
        print(data)
        return JsonResponse({'data':data},safe=False)












# FunctionBase View
# def PostDetails(request,id):
#     post = get_object_or_404(Blog,id=id)
#     context={
#         'post':post
#     }
#     return render(request,'dashboard/dashboard_posts_detail.html',context)
    





































def dashboard_categories(request):
    
    
    return render(request,'dashboard/dashboard_categories.html')




def dashboard_users(request):
    
    
    return render(request,'dashboard/dashboard_users.html')



def dashboard_comments(request):
    
    
    
    return render(request,'dashboard/dashboard_comments.html')
    