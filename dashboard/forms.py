from blogs.models import Blog,Category
from django.contrib.auth.models import User
from accounts.models import BlogUser
from django import forms
from django.conf import settings
 
#inheriting account.forms CreateUserForm for CreateUser for dashboard
from django.contrib.auth.forms import UserCreationForm

#Password Generate
import secrets
import string

# sending email import
from django.core.mail import send_mail
#error showing for try except
from smtplib import SMTPException
# importing settings to get the email_host_user NOTE: this avoid hardcoding email_from
from django.conf import settings






"""BLOG FORMS"""

#NOTE: ERROR ENCOUNTER ---> HOW TO ACCEPT FILE eg. picture FROM fetch api from js 
"""
SOLUTION: 
"""
class BlogFeaturedImage(forms.ModelForm):
    class Meta:
        model= Blog
        fields= ('featured_image',)
        
    # Image Validation (Type + Size)
    def clean_featured_image(self):
        image = self.cleaned_data.get('featured_image')

        # Image is OPTIONAL
        if not image:
            return image

        # Size validation (5MB max)
        max_size = 5 * 1024 * 1024
        if image.size > max_size:
            raise forms.ValidationError("Image size must not exceed 5MB.")
        
        return image
        
        

class BlogDetailForm(forms.ModelForm):
    class Meta:
        model = Blog
        
        #TO BE ABLE TO UPDATE THE SLUGFIELD, since it is forking in the title def save() from models.py is the reason --> check notes inside the dashboard/views.py for POST 
        
        fields = ('title','category','author','status','is_featured','short_description','blog_body')
        # widgets={
        #     'title':forms.TextInput(attrs={'required':False}),
        # }
        
        
class CreateBlogForm(forms.ModelForm):
    class Meta:   
        model=Blog
        fields = ('title','category','status','is_featured','short_description','blog_body','featured_image')
        
        



"""CATEGORY FORMS"""

class CreateCategoryForm(forms.ModelForm):
    category_description = forms.CharField(max_length=150, required=False)
    class Meta:
        model=Category
        fields=('category_name','category_description')





"""User Form"""
# NOTE: This form is inherited from account.forms, need to modify it to remove password1 and password2 since I generate a random password,  *Also implemented account expiration if the user doesn`t change the random password.


class DashboardCreateUserForm(forms.ModelForm):
    
    password1 = None
    password2 = None
    
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','is_active','is_staff']

    
    ##NOTE: the functions below we set is as static via @staticmethod --> purpose is for the function to behave as regular function not expecting (self) as parameter, function in a class is expecting self as parameter. in this approach we can define a function without putting self as parameter.
    
    #Generate temporary password using secrets and string library
    @staticmethod
    def generate_temp_password(length=10):
        chars = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(chars) for _ in range(length))
        # print(f"Your temporary password : {password}")
        return password
    
    
    # Send Email Method
    @staticmethod
    def send_email(first_name,last_name,email,temp_password):
         #send email
        try:
            send_mail(
                subject="Your Account Has Been Created",
                message=f"Hello {first_name} {last_name},\n\nYour temporary password is: {temp_password}\nPlease change it after logging in.",
                from_email=settings.EMAIL_HOST_USER, # instead of hardcoded email_from --> we get the email setup as host
                recipient_list=[email],
                fail_silently=False,
            )
        except SMTPException as e:
            print(f'SMTP error: {e}')
        except Exception as e:
            print(f'Other error: {e}')
 



"""PROFILE FORMS"""

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(max_length=50, required=False)
    
    
    class Meta:
        model=User
        fields=('first_name','last_name','email','is_active','is_staff','username')
       

class AvatarForm(forms.ModelForm):
    
    class Meta:
        model=BlogUser
        fields=('avatar','mobile')
        
