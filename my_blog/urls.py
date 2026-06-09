"""
URL configuration for my_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

from django.conf import settings # import this for dynamic path for media
from django.conf.urls.static import static # import this for dynamic path for media
from blogs import views as BlogsView
from accounts import views as AccountView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='home'),
    path('category/',include('blogs.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('register/',AccountView.register,name='register'),
    path('login/',AccountView.login,name='login'),
    path('logout/',AccountView.logout,name='logout'),
    path('<slug:slug>/',BlogsView.blogs, name='blogs'),
    path('blog/search/',BlogsView.search, name='search'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    