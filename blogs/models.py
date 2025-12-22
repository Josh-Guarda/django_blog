from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return self.category_name
    
    #If Model Name is Incorrectly spell in admin dashboard
    class Meta:
        verbose_name_plural = 'Categories'
        
STATUS_CHOICES= (
    ('Draft','Draft'),
    ('Published','Published')
)  
        
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150,unique=True, blank=True) # Slug is the - in the url This-is-My-first-Blog --> this should automatically created check setup in your admin.py
    category=models.ForeignKey(Category,on_delete=models.CASCADE)# if you delete the Category all Blog under that Category is deleted
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d') # the Image uploaded will go to this directory NOTE: this directory will be create automatically using the declared name in upload_to
    short_description= models.TextField(max_length=500)
    blog_body=models.TextField(max_length=2000)
    status = models.CharField(choices=STATUS_CHOICES, default='Draft')  # the model field will depend on the choices since we use 0,1 as value that is why we use IntegerField
    is_featured= models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title