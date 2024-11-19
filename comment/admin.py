from django.contrib import admin
from comment.models import Comment

# Register your models here.


@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display =  ['post' , 'author' , 'comment' , 'created_at' , 'updated_at' , 'created_by' , 'updated_by']