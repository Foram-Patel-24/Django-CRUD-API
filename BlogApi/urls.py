"""
URL configuration for BlogApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path , include
from rest_framework import routers
# from User import views
# from Post import views
# from comment import views
from Category import views

router = routers.DefaultRouter()

# router.register('userviewset' , views.UserViewSet , basename='user')
# router.register('postviewset' , views.PostViewSet , basename='post')
# router.register('commentviewset' , views.CommentViewSet , basename='comment')
router.register('categoryviewset' , views.CategoryViewSet , basename='category') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include(router.urls)),    
]
