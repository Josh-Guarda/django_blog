from blogs.models import Blog
from django import forms
 
 

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
        
        

class ProfileForm(forms.ModelForm):
    contact_number = forms.TextInput
    class Meta:
        fields=('first_name','last_name','email','date_joined','mobile')
        