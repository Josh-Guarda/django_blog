from django.contrib import admin
from .models import Category,Blog
# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    list_display=('title','category','author__first_name','status','is_featured')
    search_fields=('title','category__category_name','author__first_name','status')
    prepopulated_fields = {'slug':('title',)} # Automation of Slug using different field

    
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)

