from django.db.models import Count, Q
from .models import Category

def get_categories_with_count():
    return Category.objects.annotate(
        post_count=Count('blog', filter=Q(blog__status='Published'))
        
    )