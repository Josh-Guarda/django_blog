from django.contrib import admin
from django.http import HttpRequest
from .models import Category,Blog,About,Socials
# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    list_display=('title','category','author__first_name','status','is_featured') #we need to specify the foreign key field to use <FK>__<Fk field>
    search_fields=('title','category__category_name','author__first_name','status')
    prepopulated_fields = {'slug':('title',)} # Automation of Slug using different field
    
    
# Custom Model Class to Limit entry to the Admin Panel, Meaning only 1 Input is required, if there is already and Input the Add About button inside the admin page will be invisible    
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self,request): #dont remove this, the function expects 2 arguments --> if remove once click in about detail inside the Admin App will crash due to unrecognize method, since GET request is initialize that is why we passed request.
        count= About.objects.all().count()
        if count == 0:
            return True
        else:
            return False 
    
    
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Socials)


