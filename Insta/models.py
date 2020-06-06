from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField

# Create your models here.

class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        options={'quality': 100},
        null=True,
        blank=True,
        )

    def get_connections(self):
        connections = UserConnection.objects.filter(creator=self)
        return connections

    def get_followers(self):
        followers = UserConnection.objects.filter(following=self)
        return followers

    def is_followed_by(self, user):
        followers = UserConnection.objects.filter(following=self)
        return followers.filter(creator=user).exists()

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

    def __str__(self):
        return self.username


class UserConnection(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name="friendship_creator_set")
    following = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name="friend_set")

    def __str__(self):
        return self.creator.username + ' follows ' + self.following.username

class Post(models.Model):
    author = models.ForeignKey( # a foreign key indicate a Many-To-One relationship
        InstaUser, #foreign key is InstaUser
        blank=True,
        null=True,
        on_delete=models.CASCADE, # delete this author will delete all his posts
        related_name='posts', # we can use author.posts to get all posts belong to this user
        )
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
        )
    posted_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])

    def get_like_count(self):
        return self.likes.count()

    def get_comment_count(self):
        return self.comments.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments',)
    user = models.ForeignKey(InstaUser, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.comment

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes',)
    user = models.ForeignKey(InstaUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return 'Like: ' + self.user.username + ' ' + self.post.title




# from django.db import models

# from imagekit.models import ProcessedImageField

# from django.urls import reverse

# from django.contrib.auth.models import AbstractUser

# # Create your models here.
# class InstaUser(AbstractUser):
#     profile_pic = ProcessedImageField(
#         upload_to = 'static/images/profiles',
#         format = 'JPEG',
#         options = {'quality': 100},
#         blank = True,
#         null = True
#         ) 

# #子类Post继承父类models，调动属性和方法
# class Post(models.Model):
#     #定义发布人属性
#     author = models.ForeignKey(
#         InstaUser,
#         on_delete = models.CASCADE,
#         related_name = 'my_posts'
#     )
#     #第一句话定义title可以为空
#     title = models.TextField(blank=True, null=True)
#     image = ProcessedImageField(
#         upload_to='static/images/posts',
#         format='JPEG',
#         options={'quality': 100},
#         blank=True,
#         null=True,
#         )



#     #添加absolute_url，reverse是url library的方法,功能是跳转到添加的url，这里的url是model_detail
#     def get_absolute_url(self):
#         return reverse("post_detail", args=[str(self.id)])
#      #获取点赞数
#     def get_like_count(self):
#         return self.likes.count()
    


# class Like(models.Model):
#     post = models.ForeignKey(
#         Post,
#         #当user取消点赞的时候，让user与这张post整个取消关联
#         on_delete = models.CASCADE,
#         #可以找到所有like这个的object的user的name
#         related_name = 'likes'
#         )
#     user = models.ForeignKey(
#         InstaUser,
#         #当user取消点赞的时候，让user与这张post整个取消关联
#         on_delete = models.CASCADE,
#         #可以找到这个用户所有点过like的object的名字
#         related_name = 'likes'
#         )
#     #这个类是定义一个user和一个post之间只能有一个独一无二的组合，即一个人给一个post只能点一个赞
#     class Meta:
#         unique_together = ("post", "user")

#     def __str__(self):
#         return 'Like: ' + self.user.username + ' ' + self.post.title
    
