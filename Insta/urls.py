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
# #从Insta app 里面的 views文件 import HelloWorld这个类
# from Insta.views import HelloWorld, PostsView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

# urlpatterns = [
#     #当输入路径后，会调动子类HelloWorld里面as_view这个function
#     path('', HelloWorld.as_view(), name='helloworld'),
#     path('posts/', PostsView.as_view(), name='posts'),
#     #因为和上面两个路径都是post，所以为了让系统识别出不同，加上<int:pk>会传给post一个primary key用来识别不同的posts
#     path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
#     path('post/new/',PostCreateView.as_view(), name = 'make_post'),
#     path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
#     path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
# ]


from django.urls import path

from Insta.views import (EditProfile, ExploreView, PostCreateView,
                         PostDeleteView, PostDetailView, PostListView,
                         PostUpdateView, SignUp, UserProfile, addComment,
                         addLike, toggleFollow)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('post/new/', PostCreateView.as_view(), name='make_post'),
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name='edit_post'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
    path('auth/signup', SignUp.as_view(), name='signup'),
    path('user_profile/<int:pk>/', UserProfile.as_view(), name='profile'),
    path('edit_profile/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
    path('togglefollow', toggleFollow, name='togglefollow'),
    path('like', addLike, name='addLike'),
    path('comment', addComment, name='addComment'),
    path('explore', ExploreView.as_view(), name='explore'),
]