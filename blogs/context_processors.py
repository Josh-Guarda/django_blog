#This method called context_processors is a method to use a specific context/query object from a certain view function to access it to a different view
# --> in this example we are going to use # categories = Category.objects.all() from my_blog/views.py/home() returning context including category. access it to blogs/views.py/posts_by_category() NOTE: this avoids declaring explicitly on every view AVOID REPEATITION

from .models import Category,Socials

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_socials(request):
    socials = Socials.objects.all()
    return dict(socials=socials)