from django.urls import path
from . import views

from django.conf import settings # import this for dynamic path for media
from django.conf.urls.static import static # import this for dynamic path for media

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    # path('posts/',views.dashboard_posts, name='dashboard_posts'),
    # path('posts/<int:id>/',views.PostDetails,name="post_detail"),
    
    #ClassBase View
    # path('posts/',views.PostView.as_view(), name='dashboard_posts'),
    # path('posts/<int:id>/',views.PostDetailView.as_view()),
    
    
    #Modal
    path('posts/',views.PostView.as_view(), name='dashboard_posts'),
    path('<int:pk>/',views.get_data,name='posts_object'), # type: ignore
    
    
    path('categories/',views.dashboard_categories, name='dashboard_categories'),
    path('users/',views.dashboard_users, name='dashboard_users'),
    path('comments/',views.dashboard_comments, name='dashboard_comments'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
