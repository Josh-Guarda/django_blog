from django.urls import path
from . import views



urlpatterns = [
    path('<int:category_id>/',views.posts_by_category,name='posts_by_category'),
    # path('<int:post_id>/', views.save_post, name='save_post'), # type: ignore
    path('save/<int:post_id>/', views.save_post, name='save_post'), # type: ignore
]

