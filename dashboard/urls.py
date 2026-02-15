from django.urls import path
from . import views

from django.conf import settings # import this for dynamic path for media
from django.conf.urls.static import static # import this for dynamic path for media

#Setting up Login Required for ClassBase View
# from django.contrib.auth.decorators import login_required,permission_required # imports to use auth decorators.
# #NOTE: Once @login_required is initialize we need to setup a redirection path to the settings.py





urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    # path('posts/',views.dashboard_posts, name='dashboard_posts'), #FunctionBase View
    # path('posts/<int:id>/',views.PostDetails,name="post_detail"),
    
    #ClassBase View
    # path('posts/',views.PostView.as_view(), name='dashboard_posts'),
    # path('posts/<int:id>/',views.PostDetailView.as_view()),
    
    
    
    #Modal
    path('posts/',views.PostView.as_view(), name='dashboard_posts'),
    path('posts/batch-delete/',views.PostBatchDeleteView.as_view(), name='posts-batch-delete'),
    path('posts/create/',views.create_post, name='create_post'),
    path('posts/<int:pk>/',views.get_data,name='posts_object'),# Handles (READ,UPDATE,DELETE)
    
    #Profile
    path('profile/<int:user_id>',views.user_profile,name='user_profile'),
    
    path('categories/',views.dashboard_categories, name='dashboard_categories'),
    path('users/',views.dashboard_users, name='dashboard_users'),
    path('comments/',views.dashboard_comments, name='dashboard_comments'),
]   

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

