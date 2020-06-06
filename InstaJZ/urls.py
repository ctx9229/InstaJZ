#全局url设定
"""InstaJZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import include, path
# from Insta.views import Signup
from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     #如果传进来的路径包括insta，那就调用app级别的Insta.urls文件
#     path('insta/', include('Insta.urls')),
#     path('auth/', include('django.contrib.auth.urls')),
#     #定义signup的view
#     path('auth/sign', Signup.as_view(), name = 'signup'),
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Insta.urls')),
    path('auth/', include('django.contrib.auth.urls'))
]