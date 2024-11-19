from django.db import models
from Post.models import Post
from User.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE , related_name='category_created_by')
    updated_by = models.ForeignKey(User,on_delete=models.SET_NULL , null=True , related_name='category_updated_by')
    deleted = models.IntegerField(default=0)