from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from blogs.models import Blog,Category
from django.contrib.auth.models import User
#using core django generic views

from django.views.generic import TemplateView,View,ListView,DetailView
# from django.core import serializers
from django.http import JsonResponse,HttpResponseNotFound
import json
from .forms import BlogDetailForm,BlogFeaturedImage

#Importing this function to reflect all changes to django Recent Actions
from django.contrib.admin.models import CHANGE,DELETION,ADDITION 
from .helper import log_admin_action 

#Authentication and Rules
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin # Permission for ClassBase Views
from django.contrib.auth.decorators import login_required,permission_required # imports to use auth decorators.
#NOTE: Once @login_required is initialize we need to setup a redirection path to the settings.py
from django.contrib import messages # messages




@login_required
# @permission_required('dashboard.dashboard',raise_exception=True)
def dashboard(request):
    return render(request,'dashboard/dashboard.html')



# FunctionBase View
# @login_required
# @permission_required('dashboard.dashboard_posts',raise_exception=True)
# def dashboard_posts(request):
#     if request.user.is_authenticated:
#         if request.user.is_staff ==False:
#             Posts = Blog.objects.filter(author=request.user)
            
#             context = {
#                 'Posts':Posts
#             }
#             return render(request,'dashboard/dashboard_posts.html',context)
            
#         else:
#             Posts = Blog.objects.all()
#             context = {
#                 'Posts':Posts
#             }
#             # print(Posts)
#             return render(request,'dashboard/dashboard_posts.html',context)


# #ClassBase View using generic in core django NOTE: Follow the format below
class PostView(LoginRequiredMixin,ListView):
# class PostView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    #To Implement Permission we Use PermissionRequiredMixin. permission_required should be included on
    """
    #Correct Format for Permission_required declaration
    #<app_label>.<action>_<modelname>
    
    Methods are:
    - blog.view_blog
    - blog.delete_blog
    - blog.add_blog
    - blog.change_blog
    """
# class PostView(LoginRequiredMixin,PermissionRequiredMixin,ListView): 
    # permission_required = ("dashboard.view_blog","dashboard.delete_blog","dashboard.add_blog","dashboard.change_blog")
    raise_exception = True
    model = Blog
    template_name = 'dashboard/dashboard_posts.html'  # Template that we will call
    context_object_name = 'posts' # This refers on the Loop object that we loop in our template
    
    #This is the function that will run the Query Set
    def get_queryset(self):
        # Return Posts queryset if staff vs non staff
        if self.request.user.is_authenticated:
            if self.request.user.is_staff ==False:
                Posts = Blog.objects.filter(author=self.request.user)
                return Posts
                
            else:
                Posts = Blog.objects.all()
                # print(Posts)
                return Posts

        

#DISPLAY DATA ON A SEPARATE PAGE

#Temporary commented this since my Target is to pass the data-id to a modal 
#Note: that this PosDetailView is correct if we are dealing with a separate template
# class PostDetailView(DetailView):
#     model = Blog
#     template_name = 'dashboard/dashboard_posts_detail.html'




#CREATE POST
# @login_required
# @permission_required('dashboard.add_blog',raise_exception=True)
def create_post(request):
    if request.method =='GET':
        post= {
            'id':'',
            'title':"",
            'status':"",
            'short_description':"",
            'blog_body':"",
            'featured_image':"",
            'is_featured':"",
            'category':"",   
            'author':"", 
        }
        categories = list(Category.objects.values('id', 'category_name'))
        post = json.dumps(post)
        return JsonResponse({'data':post,'categories':categories})
        
    if request.method =='POST':
        print('POGI SI JOSHUA')
        
        # form = BlogDetailForm(request.POST,request.FILES)
        # print(form)
        data = request.POST.copy()
        form = BlogDetailForm({'title':data.get('postTitle'), 'status':data.get('postStatus'),'category':data.get('postCategory'),'is_featured': data.get('isFeatured'),'short_description':data.get('postDesc'),'blog_body':data.get('postBody')})
        
        
        if form.is_valid():
            form.save()
            print(form)
            
            # if request.user.is_staff:
            #     log_admin_action(
            #         user=request.user,
            #         obj=post,
            #         action_flag=CHANGE,
            #         message="Updated via custom dashboard",
            #     )
            
            return JsonResponse({'message':'Post Created Successfully'})
        
        else:
            return JsonResponse(form.errors, safe=False, status=200)
    
    return JsonResponse(
        {'status': 'error', 'message': 'Invalid request method'},
        status=405
    )
    
    




#VIEW/UPDATE/DELETE POST
@login_required
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
            'category',   #For display of category_id as current_selected for Edit
            'author',     #For display of author User_id as current_selected for Edit
            'category__category_name', #For display of category_name for VIEW
            'author__first_name', #For display of first_name for VIEW
            'author__last_name' #For display of last_name for VIEW
            ).first()
    #qs --> is already a object instance since it is .first() so it returns the 1 id 
    print(qs)
    # print(type(qs))
    qs = json.dumps(qs)
    # print(type(qs))
    if request.method =='GET':
        categories = list(Category.objects.values('id', 'category_name'))
        authors = list(User.objects.values('id', 'first_name', 'last_name'))
        return JsonResponse({'data':qs,
                             'categories': categories,
                            'authors': authors,   
                            }
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
        
   
        post= get_object_or_404(Blog,pk=pk)
        data = request.POST.copy() #To make the POST Objects editable (this is a must)
        
        #SLUG NOTES: as you can see below the slug is not included inside the dictionary however it is still updating we have the the function def save() from dashboard/models.py that triggers the realoding of the slug and getting its value from self.title

        form = BlogDetailForm({'id':pk,'title':data.get('postTitle'), 'status':data.get('postStatus'),'category':data.get('postCategory'),'author': data.get('postAuthor'),'short_description':data.get('postDesc'),'blog_body':data.get('postBody')},instance=post) # this assigns values manually direct to its own fields.

        #TO SEE THE DETAILS ON FILE/IMAGE UPLOADING SEE DOCUMENTATION BELOW:
        blog_feat_image= BlogFeaturedImage(request.POST,request.FILES,instance=post)

        
        if form.is_valid() and blog_feat_image.is_valid():
            blog_feat_image.save()
            form.save()
            
            #THIS LOGGED POST/PUT REQUEST TO DJANGO ADMIN
            if request.user.is_staff:
                log_admin_action(
                    user=request.user,
                    obj=post,
                    action_flag=CHANGE,
                    message="Updated via custom dashboard",
                )
            
            #RESPONSE BACK TO FETCH
            return JsonResponse({'message':'UPDATE SUCCESS'})
         
        else:
            # print(form.errors)
            return JsonResponse(form.errors, safe=False, status=200)
        
        # return JsonResponse({'message':'DATA RECEIVED'})
        
    if request.method =='DELETE':
        print(request)
        # post = get_object_or_404(Blog,pk=pk)
        # post.delete()
        
        #THIS LOGGED DELETE REQUEST TO DJANGO ADMIN
        if request.user.is_staff:
            print('TEST POGI')
            # log_admin_action(
            #     user=request.user,
            #     obj=post,
            #     action_flag=DELETION,
            #     message="Deleted via custom dashboard",
            # )

        return JsonResponse({'message':'DATA Delete'})
        
        
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
            
       
        
        
    




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
    