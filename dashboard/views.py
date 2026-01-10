from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from blogs.models import Blog,Category
from django.contrib.auth.models import User
#using core django generic views

from django.views.generic import TemplateView,View,ListView,DetailView
# from django.core import serializers
from django.http import JsonResponse
import json
from .forms import BlogDetailForm,BlogFeaturedImage
from django.contrib import messages
import os # This import is use to check for image.path (for image update)

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
        
        form = BlogDetailForm({'id':pk,'title':data.get('postTitle'), 'status':data.get('postStatus'),'category':data.get('postCategory'),'author': data.get('postAuthor'),'short_description':data.get('postDesc'),'blog_body':data.get('postBody')},instance=post) # this assigns values manually direct to its own fields.
        
        
        #TO SEE THE DETAILS ON FILE/IMAGE UPLOADING SEE DOCUMENTATION BELOW:
        blog_feat_image= BlogFeaturedImage(request.POST,request.FILES,instance=post)
        
        if form.is_valid() and blog_feat_image.is_valid():
            blog_feat_image.save()
            form.save()
            messages.add_message(request,messages.INFO,'Post Successfully Updated!')
            redirect ('dashboard_posts')
            return JsonResponse({'message':'UPDATE SUCCESS'})
         
        else:
            messages.add_message(request,messages.ERROR,f'Update Failed: {str(form.errors.as_text())}')
            print(form.errors)
            return JsonResponse(form.errors, safe=False, status=200)
        # return JsonResponse({'message':'DATA RECEIVED'})
   
            
       
        
        
    




"""USEFUL IMAGE UPLOAD DOCUMENTATION"""

"""
📌 Django Image Upload (Fetch API + Dynamic Form) — Internal Documentation
Overview

This project uses Fetch API and JavaScript-generated forms instead of Django-rendered templates.
Because of this, text fields and file fields behave differently and must be handled correctly."""


"""
1️⃣ Key Rule (Most Important)

Text inputs come from request.POST
File inputs come from request.FILES

They are never interchangeable.

2️⃣ ModelForms Used

---> Image Form

    class BlogFeaturedImage(forms.ModelForm):
        class Meta:
            model = Blog
            fields = ('featured_image',)

---> Detail Form (Text / Foreign Keys / Slug)

class BlogDetailForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'title',
            'slug',
            'category',
            'author',
            'status',
            'is_featured',
            'short_description',
            'blog_body'
        )
        widgets = {
            'title': forms.TextInput(attrs={'required': False}),
        }

3️⃣ JavaScript Template (Dynamic Form)

✅ Correct Image Input (IMPORTANT)

    <input
    type="file"
    id="avatar-upload"
    name="featured_image"
    accept="image/png,image/jpeg"
    hidden
    />

❌ Incorrect (will NOT work)

    <input
    type="file"
    id="avatar-upload"
    name="featuredImage"
    accept="image/png,image/jpeg"
    hidden
    />
    
--> Why? Django matches file inputs by field name, not JS variable names.

    Model field:
    featured_image = models.ImageField(...)

    ✔ Input name must match exactly:  name="featured_image"

    
4️⃣ Why Other Fields Can Have Custom Names

    Example: Title field:
    <input type="text" name="postTitle" value="${post.title}">


--> This works because you manually map it:

    data = request.POST.copy()
    form = BlogDetailForm({
        'title': data.get('postTitle'),
        'status': data.get('postStatus'),
        'category': data.get('postCategory'),
        'author': data.get('postAuthor'),
        'short_description': data.get('postDesc'),
        'blog_body': data.get('postBody'),
    }, instance=post)


    ✔ Text fields = manual assignment is allowed
    ❌ File fields = manual assignment behaves differently

5️⃣ Why Images Do NOT Work Like Text Fields
    ❌ This does NOT work
    data.get('featuredImage')  # ALWAYS None


--> Why? Files do not exist in request.POST 
    Django stores uploaded files in request.FILES


6️⃣ Correct Way to Handle Image Upload
    ✅ Best Practice (Recommended)
    
    blog_feat_image = BlogFeaturedImage(
        request.POST,
        request.FILES,
        instance=post
    )

    ✔ Django automatically:
    
--> detects if a file was uploaded
--> updates the image
--> keeps the old image if none was uploaded

    ❌ Why this does NOT work
    BlogFeaturedImage({'featured_image': request.FILES}, instance=post)


--> Because:

    request.FILES is a MultiValueDict
    Django expects one file, not a container


7️⃣ Debug Proof (Expected Output)
    print(request.FILES)


    Output:
    <MultiValueDict: {
    'featured_image': [<TemporaryUploadedFile: 737333.png>]
    }>
    
    ✔ Correct — file exists
    ❌ request.POST['featured_image'] → None


8️⃣ Final Correct POST Handling Pattern

    if request.method == 'POST':
        data = request.POST.copy()
        post = get_object_or_404(Blog, pk=pk)

        # Text fields
        form = BlogDetailForm({
            'title': data.get('postTitle'),
            'status': data.get('postStatus'),
            'category': data.get('postCategory'),
            'author': data.get('postAuthor'),
            'short_description': data.get('postDesc'),
            'blog_body': data.get('postBody'),
        }, instance=post)

        # Image field
        blog_feat_image = BlogFeaturedImage(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid() and blog_feat_image.is_valid():
            blog_feat_image.save()
            form.save()
            return JsonResponse({'message': 'UPDATE SUCCESS'})

9️⃣ Summary Table

    FieldType	    Input name	        Source	        Handling
        title	       postTitle	    request.POST	Manual mapping
        status	       postStatus	    request.POST	Manual mapping
        category	   postCategory	    request.POST	Manual mapping
        author	       postAuthor	    request.POST	Manual mapping
    featured_image	   featured_image	request.FILES	Pass FILES to form
    
    
10️⃣ Golden Rule (Memorize This)

-->If it’s a file:
    Input name must match the model field
    File comes from request.FILES
    Pass request.FILES directly to the ModelForm
    
    
    
ADDITIONAL TO REMEMBER:

Optional Image Update (Keep Old Image)

    ✔ Automatic Behavior
    -If the user does NOT select a new image:
    -request.FILES is empty
    
    ✔ Existing image preserved
    ✔ No overwrite
    ✔ No deletion

    Django keeps the existing image No extra logic required:

    form = BlogUpdateForm(request.POST, request.FILES, instance=post)

"""






























def dashboard_categories(request):
    
    
    return render(request,'dashboard/dashboard_categories.html')




def dashboard_users(request):
    
    
    return render(request,'dashboard/dashboard_users.html')



def dashboard_comments(request):
    
    
    
    return render(request,'dashboard/dashboard_comments.html')
    