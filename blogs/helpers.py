from django.db.models import Count, Q
from .models import Category
from django.core.paginator import Paginator



def get_categories_post_count():
    return Category.objects.annotate(
        post_count=Count('blog'),
        draft=Count('blog', filter=Q(blog__status='Draft')),
        published=Count('blog', filter=Q(blog__status='Published')),
        
    )
    

def set_pagination(request, queryset, default_per_page=5):
    paginate_quant = request.GET.get('paginate_quant', default_per_page)
    page_number = request.GET.get('page', 1)
    
    try:
        paginate_quant = int(paginate_quant)
    except (ValueError, TypeError):
        paginate_quant = default_per_page

    paginator = Paginator(queryset, paginate_quant)
    page_obj = paginator.get_page(page_number)
    return page_obj

    
    
    

    
    

        
#     )
    
# def get_categories_count():
#     # return Category.objects.annotate(
#     #     post_count=Count('blog', filter=Q(blog__status='Published')))
#     return Category.objects.annotate(post_count=Count('blog'))