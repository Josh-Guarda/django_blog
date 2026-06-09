from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from blogs.models import Blog,Category
from accounts.models import BlogUser

#Import Group Model to assign designated group to a created user in User Model 
from django.contrib.auth.models import User,Group

from django.contrib import messages
#using core django generic views

from django.views.generic import TemplateView,View,ListView,DetailView

# from django.core import serializers
from django.http import JsonResponse,HttpResponseNotFound,HttpResponseForbidden
import json
from .forms import BlogDetailForm,BlogFeaturedImage,CreateBlogForm,ProfileForm,AvatarForm,CreateCategoryForm,DashboardCreateUserForm


#Importing this function to reflect all changes to django Recent Actions
from django.contrib.admin.models import CHANGE,DELETION,ADDITION 
from .helper import log_admin_action 

#Authentication and Rules
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin # Permission for ClassBase Views
from django.contrib.auth.decorators import login_required,permission_required # imports to use auth decorators.
#NOTE: Once @login_required is initialize we need to setup a redirection path to the settings.py

# from django.contrib.auth.models import Permission #use to check perm logs
from django.core.exceptions import PermissionDenied #Permission for functionBase views

#This Count is used to get the post_count by category via get_context_data() inside PostView classBase view
from django.db.models import Count,Q

#using get_categories_with_count() from helper.py to get post_count by category for functionBase view
from blogs.helpers import get_categories_post_count,set_pagination





"""Dashboard HOME"""
@login_required
# @permission_required('dashboard.dashboard',raise_exception=True)
def dashboard(request,):
    
    return render(request,'dashboard/dashboard.html')




"""Profile"""
@login_required
def user_profile_detail(request,user_id):
    if request.user.id != user_id:
        messages.error(request, "You are not allowed to view this profile.")
        return redirect('logout')  
    
    current_user = get_object_or_404(User, id=user_id)
    
    return render(request, 'dashboard/components/dashboard_profile.html', {
        'current_user': current_user
    })


@login_required
def user_profile_edit(request, user_id):
    if request.user.id != user_id:
        messages.error(request, "You are not allowed to view this profile.")
        return redirect('logout')  
    
    current_user = get_object_or_404(User, id=user_id)
    
    if request.method =="POST":
        data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
        }
        form = ProfileForm(data,instance=current_user)
        extended_user = current_user.bloguser   # type: ignore # get existing profile
        avatar = AvatarForm(request.POST, request.FILES, instance=extended_user) # type: ignore
        
        
        if form.is_valid() and avatar.is_valid():
            form.save()
            avatar.save()
            
            # extended_user.mobile = request.POST.get('mobile')
            # if extended_user.mobile.is_valid():
            #     extended_user.save()

            messages.add_message(request, messages.SUCCESS, 'Profile updated successfully')
            return redirect('user_profile', user_id=user_id)
            
        else:
            
            if avatar.errors:
                messages.add_message(request, messages.ERROR, str(avatar.errors.as_text()))
            if form.errors:
                messages.add_message(request, messages.ERROR, str(form.errors.as_text()))
                
                
    return render(request, 'dashboard/dashboard_profile_update.html', {
        'current_user': current_user
    })
    

"""Profile Account Settings"""
@login_required
def user_account_settings(request,user_id):
    if request.user.id != user_id:
        messages.error(request, "You are not allowed to view this profile.")
        return redirect('logout')  
    
    current_user = get_object_or_404(User, id=user_id)
    
    return render(request,'dashboard/components/dashboard_account_settings.html',{
        'current_user': current_user,
    })


@login_required
def user_account_settings_update(request,user_id):
    if request.user.id != user_id:
        messages.error(request, "You are not allowed to view this profile.")
        return redirect('logout')  
    
    current_user = get_object_or_404(User, id=user_id)
    section = request.GET.get('section') #defines the section to execute
    
    
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'username':
            new_username = request.POST.get('username')
            # validate and save username from input type hidden
            current_user.username = new_username
            current_user.save()
            messages.add_message(request, messages.SUCCESS, "Username updated successfully.")
            
            return redirect('user_account_settings', user_id=user_id)

        elif form_type == 'password':
            # validate and save password from input type hidden
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_new_password')
            
            if not current_user.check_password(old_password):
                messages.add_message(request, messages.ERROR, "Old password is incorrect.")
            elif new_password != confirm_password:
                messages.add_message(request, messages.ERROR, "Passwords do not match.")
            else:
                current_user.set_password(new_password)
                current_user.save()
                messages.add_message(request, messages.SUCCESS, "Password updated successfully.")
                return redirect('user_account_settings', user_id=user_id)

    return render(request, 'dashboard/dashboard_account_settings_update.html', {
        'current_user': current_user,
        'section': section,
        
    })
    
    
    


"""POSTS"""

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
#class PostView(LoginRequiredMixin,ListView):
class PostView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
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
    permission_required = ("blogs.view_blog")
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
            
            
            
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.annotate(
            post_count=Count('blog')
        )
        context['categories_with_count'] = categories
        return context
            

    # #PAGINATION for ClassBaseView
    # #documentation: https://docs.djangoproject.com/en/4.2/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginate_by
    def get_paginate_by(self, queryset):
        paginate_quant = self.request.GET.get("paginate_quant",5)#get number of desired show-entries from frontend and set initial value of pagination 
        
        try:
            paginate_quant = int(paginate_quant)
        except (TypeError, ValueError):
            paginate_quant = 5

        return paginate_quant
    
    
    
    
    
    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            
            #Get request for total checksboxes and check counter per check 
            check_items = request.GET.getlist('checksItems') # fetches total checksboxes
            checked_ids = request.GET.getlist('checks') # fetches counter per check  
            checkall_ids = request.GET.getlist('checkers') # fetches counter per if checkall  
            
            total_check_items = len(check_items)
            
            if checked_ids:
                print('single check')
                total_check_items=len(check_items)
                checked = len(checked_ids)
                
                print(f'checks:{checked_ids}')
                return JsonResponse({
                'total': total_check_items,
                'checked': checked
                })
                
            if checkall_ids:
                total_check_items=len(check_items)
                checkall_total_checks = len(checkall_ids)
                print(f'checkall:{checkall_ids}')
                
                return JsonResponse({
                'total': total_check_items,
                'checked': checkall_total_checks
                })
                            
            return JsonResponse({
            'total': total_check_items,
            'checked': 0
        })

        return super().get(request, *args, **kwargs)
        

#DISPLAY DATA ON A SEPARATE PAGE
#Temporary commented this since my Target is to pass the data-id to a modal 
#Note: that this PosDetailView is correct if we are dealing with a separate template
# class PostDetailView(DetailView):
#     model = Blog
#     template_name = 'dashboard/dashboard_posts_detail.html'




#Delete Via CheckBox
class PostBatchDeleteView(LoginRequiredMixin, PermissionRequiredMixin,View):
    permission_required = "blogs.delete_blog"
    raise_exception = True
    
    
    def post(self, request):
        print(request)
        data = json.loads(request.body)
        ids = data.get('ids', [])

        if not ids:
            return JsonResponse(
                {'error': 'No posts selected'},
                status=400
            )

        qs = Blog.objects.filter(id__in=ids)

        # Optional: limit to own posts if not staff
        if not request.user.is_staff:
            qs = qs.filter(author=request.user)

        deleted_count, _ = qs.delete()

        return JsonResponse({
            'deleted': deleted_count
        })



#CREATE POST
@login_required
# @permission_required('blogs.add_blog', raise_exception=True)
def create_post(request):
    # perm = Permission.objects.filter(content_type__app_label="blogs")
    # print(perm)
    
    # if request.user.is_staff:
    #     return HttpResponseForbidden("Admins cannot create posts")
    if request.method =='GET':
        if not request.user.has_perm('blogs.add_blog'):
            raise PermissionDenied
            
    # if not request.user.has_perm('blogs.add_blog'):
    #     print('YOU DONT HAVE ALL PERMISSION')
    #     return JsonResponse(
    #     {'message': 'You do not have permission to do this action'},
    #     status=403
    #     )
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
        if not request.user.has_perm('blogs.add_blog'):
            # print('YOU DONT HAVE POST PERMISSION')
            raise PermissionDenied
        
        data = {
            'title': request.POST.get('postTitle'),
            'category': request.POST.get('postCategory'),
            'status': request.POST.get('postStatus'),
            'short_description': request.POST.get('postDesc'),
            'blog_body': request.POST.get('postBody'),
        }

        form = CreateBlogForm(data,request.FILES) 
        
        # print(form)
        if form.is_valid():
            # print(form)
            post = form.save(commit=False) # Light save/not save yet to the db since we will assign another value author
            post.author = request.user  # set system-controlled field
            post.save() 
            
            return JsonResponse({'message':'Post Created Successfully'})
        else:
            print(form.errors)
            return JsonResponse(form.errors, safe=False, status=200)
    
    return JsonResponse(
        {'status': 'error', 'message': 'Invalid request method'},
        status=405
    )


#VIEW/UPDATE/DELETE POST
@login_required
# @permission_required([
#     'blogs.view_blog', 
#     'blogs.change_blog', 
#     'blogs.delete_blog']
#     ,raise_exception=True)
def get_data(request,pk):
    #QUERYSET VS OBJECT
    
    #QUERYSET
    #from django.core import serializers # -->onyly accepts qs 
    
    # qs = Blog.objects.filter(pk=pk) # return the list of all the queries / QuerySET
    # if request.method =='GET':
    #     data = serializers.serialize('json',qs) # This only accepts QuerySETS
    #     print(type(data))
    #     return JsonResponse({'data':data},safe=False)
    
    #OBJECT --> this case be return directly as the responseph time now
    
    

    """Model Object to JSON approach """
    
    #Approach 1 (Manual Filter)
    #This Approach is setting values to be converted from dict to json
    if request.user.is_staff and request.user.has_perm('blogs.view_blog'):
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
    else:
        qs = Blog.objects.filter(pk=pk,author=request.user.id).values( 
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
    
    
    
    # Approach 2
    # Setting up manual dictionary for JSON convertion
    #NOTE: Current limitation for this approach it cannot access foreign keys return NONE   --> to be tweak in the future: but this is the better approach compare to 1st approach
    
    # post = get_object_or_404(Blog,pk=pk,author=request.user)
    # qs = {
    #         'id': post.id,
    #         'title': post.title,
    #         'slug': post.slug,
    #         'status': post.status,
    #         'short_description': post.short_description,
    #         'blog_body': post.blog_body,
    #         'featured_image': post.featured_image.name,
    #         'category': post.category.id,
    #         'category_name': post.category.category_name,
    #         'author': post.author.id,
    #         'author_name': f"{post.author.first_name} {post.author.last_name}",
    #     }

    
    qs = json.dumps(qs)
    # print(type(qs))
    
    if request.method == 'GET':
        #Check for View Blog Permission
        if not request.user.has_perm('blogs.view_blog'):
            raise PermissionDenied
        
        
        #(USING THE APPROACH 1 Security is set manually)
        # Check if Post accessed is for the request.user else throw error 404
        if not qs:
            return JsonResponse(
                {'message': 'You cannot access this post'},
                status=403
            )
        
        
        categories = list(Category.objects.values('id', 'category_name'))
        authors = list(User.objects.values('id', 'first_name', 'last_name'))

        return JsonResponse({
            'data': qs,
            'categories': categories,
            'authors': authors,
        })
        
        
        ##(USING THE APPROACH 2 Security is set automatically since we use get_object_or_404 throws error 404)
        # categories = list(Category.objects.values('id', 'category_name'))
        # authors = list(User.objects.values('id', 'first_name', 'last_name'))
        # return JsonResponse({'data':qs,
        #                     'categories': categories,
        #                     'authors': authors,   
        #                     }
        #                     ,safe=False)
        
        
        
    elif request.method == 'POST':
        #Check for Change Blog Permission
        if not request.user.has_perm('blogs.change_blog'):
            raise PermissionDenied
        
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
            return JsonResponse({'message':'UPDATE POST SUCCESS'})
         
         
        else:
            # print(form.errors)
            # return JsonResponse(form.errors, safe=False, status=200)
            
            #checking error items
            errors = form.errors.get_json_data() # display error as dictionary. --> {'category_name': [{'message': 'Ensure this value has at most 50 characters (it has 133).', 'code': 'max_length'}]}
            
            #iterate to errors.items()
            clean_errors = []
            for field, messages in errors.items():
                for err in messages:
                    clean_errors.append(f"{field}: {err['message']}")
            # print(clean_errors)
            
            return JsonResponse({
                'message': 'Validation failed',
                'errors': clean_errors
            }, status=400)
        
        
    elif request.method == 'DELETE':
        #Check for Delete Blog Permission
        if not request.user.has_perm('blogs.delete_blog'):
            raise PermissionDenied
            # print("You do not have permission to do this action")
            # return JsonResponse(
            # {'message': 'You do not have permission to do this action'},
            # status=403
            # )
        
        post = get_object_or_404(Blog,pk=pk)
        post.delete()
        
        #THIS LOGGED DELETE REQUEST TO DJANGO ADMIN
        if request.user.is_staff:
            log_admin_action(
                user=request.user,
                obj=post,
                action_flag=DELETION,
                message="Deleted via custom dashboard",
            )
        
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




"""Categories"""
@login_required
@permission_required('blogs.view_category', raise_exception=True)
def dashboard_categories(request):
    if request.user.is_authenticated and request.user.is_staff:
        categories = get_categories_post_count()
        page_obj = set_pagination(request, categories)

        context = {
            'page_obj': page_obj,
        }
    return render(request, 'dashboard/dashboard_categories.html', context)


@login_required
@permission_required('blogs.add_category',raise_exception=True)
def dashboard_add_categories(request):
    if request.user.is_authenticated and request.user.is_staff:
        categories = get_categories_post_count()
        page_obj = set_pagination(request, categories)
        
        section = request.GET.get('section') # !important need to declare this to get the section declared in the anchor tag. for section='addNewCategory'
        
    if request.method =='POST':
        category_data = {
            'category_name': request.POST.get('category_name'),
            'category_description': request.POST.get('category_description')
        }
        category_form = CreateCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.add_message(request, messages.SUCCESS, 'Category created successfully')
            return redirect('dashboard_categories')
        else:
            messages.add_message(request, messages.ERROR, str(category_form.errors.as_text()))
            
    context = {
        'page_obj': page_obj,
        'section':section
    }
    return render(request, 'dashboard/dashboard_create_category.html', context)



@login_required
def get_category_data(request,pk):
    if not request.user.is_staff or not request.user.has_perm('blogs.change_category'):
        raise PermissionDenied
    else:
        if request.method =='GET':
            
            qs = Category.objects.filter(pk=pk).values( 
                'id',
                'category_name',
                'category_description',
                ).first()
            
            qs = json.dumps(qs) # convert object/dict to JSON formated string
            return JsonResponse({'data':qs,})
            # else:
                # return JsonResponse({'data':'Permission Denied: Contact Administrator'})

        if request.method == 'POST':
            #Permission Validation
            if not request.user.has_perm('blogs.change_category'):
                raise PermissionDenied
            

            category = get_object_or_404(Category,pk=pk)
            data = request.POST.copy()
            form = CreateCategoryForm({'id':pk,'category_name':data.get('category_name'), 'category_description':data.get('category_description')},instance=category) # this assigns values manually direct to its own fields.

            if form.is_valid():
                form.save()
                
                #THIS LOGGED POST/PUT REQUEST TO DJANGO ADMIN
                if request.user.is_staff:
                    log_admin_action(
                        user=request.user,
                        obj=category,
                        action_flag=CHANGE,
                        message="Updated via custom dashboard",
                    )

                #RESPONSE BACK TO FETCH
                return JsonResponse({'message':'UPDATE SUCCESS'})
            
            else:
                #checking error items
                errors = form.errors.get_json_data() # display error as dictionary. --> {'category_name': [{'message': 'Ensure this value has at most 50 characters (it has 133).', 'code': 'max_length'}]}
                
                #iterate to errors.items()
                clean_errors = []
                for field, messages in errors.items():
                    for err in messages:
                        clean_errors.append(f"{field}: {err['message']}")
                # print(clean_errors)
                
                return JsonResponse({
                    'message': 'Validation failed',
                    'errors': clean_errors
                }, status=400)  #  #return status code 400 Bad Request--> when this is passed fetch complete and read as not modified PREVENT SweetAlert to show.
        
        
        if request.method == 'DELETE':
            if not request.user.has_perm('blogs.delete_category'):
                raise PermissionDenied
            
            category = get_object_or_404(Category,pk=pk)
            category.delete()
            
            #THIS LOGGED DELETE REQUEST TO DJANGO ADMIN
            if request.user.is_staff:
                log_admin_action(
                    user=request.user,
                    obj=category,
                    action_flag=DELETION,
                    message="Deleted via custom dashboard",
                )
            
            return JsonResponse({'data':'Delete success'})
        
        return JsonResponse({'message':'Error on getting category data'})
    
    
    






"""Users"""
@login_required
def dashboard_users(request):
    if not request.user.has_perm('auth.view_user') or request.user.is_anonymous:
        raise PermissionDenied
    else:
        users = User.objects.filter(is_superuser=False) # Display all users aside from SuperUser/Admin account
        # users = User.objects.filter()
        page_obj = set_pagination(request, users)
        
        context = {
            'page_obj': page_obj,
        }

    return render(request,'dashboard/dashboard_users.html',context)



def dashboard_add_users(request):
    # fields = User._meta.get_fields() #Command to get all the fields of a Django builtin Model
    # print(fields)
    if not request.user.has_perm('auth.add_user') or request.user.is_anonymous:
        raise PermissionDenied
    else:
        group = Group.objects.all()
        if request.method =="POST":
            data= {
                'first_name':request.POST.get('first_name'),
                'last_name':request.POST.get('last_name'),
                'email':request.POST.get('email'),
                'username':request.POST.get('username'),
                'is_active': bool(request.POST.get('status')), # by converting to boolean value is True or False instead of default On/Off
                'is_staff': bool(request.POST.get('staff')),   # by converting to boolean value is True or False instead of default On/Off
                'selected_group':request.POST.get('accessType'),
            }
            form = DashboardCreateUserForm(data)
            # print(request.POST)
            # print(request.FILES)
            
            if form.is_valid():
                #1. Create an instance object without saving yet
                user = form.save(commit=False)
                #2. Generate Temporary password for User created
                temp_password = DashboardCreateUserForm.generate_temp_password(10) #initialize generate random password
                #3. Validate temp_password using set_password method
                user.set_password(temp_password)
                # 4. Create The User Object then use the user instance to access bloguser
                user.save()
                created_user = user.bloguser # assign object user to created_user and access the foreign connection as .bloguser NOTE: userprofile in BlogUser model is automatically created when a user is created via @receiver. CHECK accounts/models.py for more info.
                
                #5 Initialize ProfileForm
                profile_form = AvatarForm(request.POST, request.FILES,instance=created_user) # use created_user object as instance to prevent duplicate creation, else it might cause CONSTRAINT error.
                
                #6. Save profile_form input if is_valid() ==YES, NOTE: This doesnt save a profile as new object since we use the created_user instance as the current object basically we are updating the object.
                if profile_form.is_valid():
                    profile = profile_form.save(commit=False)
                    profile.user = user 
                    profile.save()
                    #7. Retrieve the target group and Add the user to the group 
                    designated_group = Group.objects.get(name=data['selected_group'])
                    user.groups.add(designated_group)
                    #8. Send welcome email containing temporary password to email inputed
                    DashboardCreateUserForm.send_email(
                                                        first_name=data['first_name'],
                                                        last_name=data['last_name'],
                                                        email=data['email'],
                                                        temp_password=temp_password)
                    messages.add_message(request, messages.SUCCESS, 'Profile created successfully') # type: ignore
        
                if profile_form.errors:
                    errors = profile_form.errors.get_json_data()
                    clean_errors = []

                    for field, field_errors in errors.items():
                        for err in field_errors:
                            clean_errors.append(f"{field}: {err['message']}")
                    messages.error(request, " | ".join(clean_errors))
            else:
                if form.errors:
                    errors = form.errors.get_json_data()
                    clean_errors = []

                    for field, field_errors in errors.items():
                        for err in field_errors:
                            clean_errors.append(f"{field}: {err['message']}")
                    messages.error(request, " | ".join(clean_errors))

                
    
        context={
            'group':group,
        }
        
        return render(request,'dashboard/dashboard_user_create.html',context)
        



def get_user_data(request,pk):
    if request.user.is_staff and request.user.has_perm('auth.change_user'):
        user = get_object_or_404(User, pk=pk)

        #How to pass dynamic options on a selection e.g Groups Model
        #1. Query Groups model to get query set.
        all_group = Group.objects.all()
        #2. make a list of the query set then pass this on the qs dict NOTE: the object will be passed in JS as list and need to access it via map
        all_group=list(all_group.values())
        #How to get dynamic user group assignment
        #1. get the user's current group id (first group only) # use the object query at the top
        user_group = user.groups.first()
        user_group_id = user_group.id if user_group else 2  # default to 2 (Manager) if no group assigned
        # print(user_group_id)

        qs = {
            'avatar': user.bloguser.avatar.url,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'username': user.username,
            'mobile': user.bloguser.mobile,
            'is_active': user.is_active,
            'is_staff': user.is_staff,
            'groups': all_group,
            'user_group_id': user_group_id,  # ← add this
        }
        
        
        if request.method == 'GET':
            # qs = json.dumps(qs)
            # return JsonResponse({'data': qs})
            
            qs = json.dumps(qs)
            return JsonResponse({'data': qs})
        
        if request.method == 'POST':
            
            if user.is_superuser:
                raise PermissionDenied
            
            data = request.POST.copy() #To make the POST Objects editable (this is a must)
            form = ProfileForm({'id':pk,'first_name':data.get('first_name'),'last_name':data.get('last_name'),'email':data.get('email'),'username': data.get('username'),'is_active':data.get('status'),'is_staff':data.get('staff')},instance=user) # this assigns values manually direct to its own fields.
            
            
            
            extended_user = user.bloguser   # type: ignore # get existing profile
            avatar = AvatarForm(request.POST, request.FILES, instance=extended_user) # type: ignore
            
            if form.is_valid():
                form.save() 
                avatar.save()
                
                #UPDATE GROUP ASSIGNMENT
                # Groups is a ManyToMany field, functions to use are: .set() -> Update, .add() -> ADD, or .remove() -> remove
                selected_group = request.POST.get('accessType')
                designated_group = Group.objects.get(id=selected_group)
                user.groups.set([designated_group])
                
                #THIS LOGGED POST/PUT REQUEST TO DJANGO ADMIN
                if request.user.is_staff:
                    log_admin_action(
                        user=request.user,
                        obj=user,
                        action_flag=CHANGE,
                        message="Updated via custom dashboard",
                    )
                
                #RESPONSE BACK TO FETCH
                return JsonResponse({'message':f'{user.first_name} {user.last_name}`s profile updated successfully '})
            
            else:
                #checking error items
                errors = form.errors.get_json_data() # display error as dictionary. --> {'category_name': [{'message': 'Ensure this value has at most 50 characters (it has 133).', 'code': 'max_length'}]}
                
                #iterate to errors.items()
                clean_errors = []
                for field, messages in errors.items():
                    for err in messages:
                        clean_errors.append(f"{field}: {err['message']}")
                print(clean_errors)
                
                return JsonResponse({
                    'message': 'Validation failed',
                    'errors': clean_errors
                }, status=400)
                
                
        if request.method =='DELETE':
            if not request.user.has_perm('auth.delete_user'):
                raise PermissionDenied
            
            if user.is_superuser:
                raise PermissionDenied
            
            else:
                user.delete()
                #THIS LOGGED DELETE REQUEST TO DJANGO ADMIN
                if request.user.is_staff:
                    log_admin_action(
                        user=request.user,
                        obj=user,
                        action_flag=DELETION,
                        message="Deleted via custom dashboard",
                    )
                
                return JsonResponse({'data':'Delete success'})
                    
     
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
    
    else:
        raise PermissionDenied






"""Save Posts"""
def dashboard_save_post(request):
    
    
    
    
    
    
    
    
    
    
    return render(request,'dashboard/dashboard_save_post.html')








"""Comments"""
def dashboard_comments(request):
    
    
    return render(request,'dashboard/dashboard_comments.html')












    