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
        

class BlogDetailForm(forms.ModelForm):
    class Meta:
        model = Blog
        
        #TO BE ABLE TO UPDATE THE SLUGFIELD, since it is forking in the title, just include in inside the fields --> check notes inside the dashboard/views.py for POST 
        
        fields = ('title','slug','category','author','status','is_featured','short_description','blog_body')
        widgets={
            'title':forms.TextInput(attrs={'required':False}),
        }
        
        
    
        
        
        