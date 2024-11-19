from django.db import models
from Post.models import Post
from User.models import User
from django.utils.timezone import now

# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='comments')
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_author')
    comment = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE , related_name='comment_created' , null=True)
    updated_by = models.ForeignKey(User,on_delete=models.SET_NULL , null=True , related_name='comment_updated')
    deleted = models.IntegerField(default=0)