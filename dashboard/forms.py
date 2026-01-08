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
        fields = ('title','status','category','author','is_featured','short_description','blog_body')
        
        
    
        
        
        