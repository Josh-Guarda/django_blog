from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from blogs.models import Blog,Category
from django.contrib.auth.models import User
#using core django generic views

from django.views.generic import TemplateView,View,ListView,DetailView
from django.core import serializers
from django.http import JsonResponse
import json
from .forms import BlogDetailForm,BlogFeaturedImage
from django.contrib import messages
from django.forms import model_to_dict
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
    #QUERYSET VS OBJECT
    
    #QUERYSET
    #from django.core import serializers # -->onyly accepts qs 
    
    # qs = Blog.objects.filter(pk=pk) # return the list of all the queries / QuerySET
    # if request.method =='GET':
    #     data = serializers.serialize('json',qs) # This only accepts QuerySETS
    #     print(type(data))
    #     return JsonResponse({'data':data},safe=False)
    
    
    #OBJECT --> this case be return directly as the response
    qs = Blog.objects.filter(pk=pk).values( 
            'id',
            'title',
            'slug',
            'status',
            'short_description',
            'blog_body',
            'featured_image',
            'category__category_name',
            'author__first_name',
            'author__last_name').first()
    #qs --> is already a object instance since it is .first() so it returns the 1 id 
    qs = json.dumps(qs)
    # print(type(qs))
    if request.method =='GET':
        
        categories = list(Category.objects.values('id', 'category_name'))
        authors = list(User.objects.values('id', 'first_name', 'last_name'))
        return JsonResponse({'data':qs,
                             'categories': categories,
                            'authors': authors,}
                            ,safe=False)

    
    if request.method =='POST':
        """
        #IMPORTANT NOTE: IF THE FORM IS BEING HANDLED ASYNCHRONOUSLY / via Modal
        
        1. create a forms that handles the model and fields involve.
        2. set error handling.
        3. for handling files follow --->
        e.g  
        post= get_object_or_404(Blog,pk=pk)
        featured_image = BlogFeaturedImage(request.POST,request.FILES,instance=post)
        
        4. IMPORTANT: since your are creating the form via js, 
        Django cannot guess the data and field mapping!!!!
        make sure to assign it manually on its respected field. 
         
        NOTE: request.POST.copy() make this conversion first
        
        ✅ Creates a MUTABLE copy of the POST data
        ✅ You can now add, change, or override fields
        ✅ Safe to pass into a ModelForm
        
        WRONG: DIRECT ASSIGNING WIHOUT COPY
         - request.POST['title'] = 'Test' --> this wont work 
        
        CORRECT: 
        data = request.POST.copy()
        data['title'] = data.get('postTitle')
        data['status'] = data.get('postStatus')
        ...
        
        """
        
 
        
        data = request.POST.copy() #To make the POST Objects editable (this is a must)
        post= get_object_or_404(Blog,pk=pk)
        
        #SLUG NOTES: as you can see below the slug is not included inside the dicutionary however it is still updating since it is declared inside the form and the most important is the function def save() from dashboard/models.py that triggers the realoding of the slug and getting its value from self.title
        
        form = BlogDetailForm({'id':pk,'title':data.get('postTitle'), 'status':data.get('postStatus'),'category':data.get('postCategory'),'author': data.get('postAuthor'),'short_description':data.get('postDesc'),'blog_body':data.get('postBody')},instance=post)
        blog_feat_image= BlogFeaturedImage({'featured_image':data.get('featuredImage')},request.FILES,instance=post)
        
        if form.is_valid() and blog_feat_image.is_valid():
            print('POGI AKO')
            
            blog_feat_image.save()
            form.save()
            messages.add_message(request,messages.INFO,'Post Successfully Updated!')
            
            return JsonResponse({'message':'UPDATE SUCCESS'})
         
        else:
            messages.add_message(request,messages.ERROR,f'Update Failed: {str(form.errors.as_text())}')
            print(form.errors)
            return JsonResponse(form.errors, safe=False, status=200)
        # return JsonResponse({'message':'DATA RECEIVED'})
   
            
       
        
        
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
    