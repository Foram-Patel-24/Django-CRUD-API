from rest_framework import serializers
from comment.models import Comment

class CmtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post' , 'author' , 'comment' , 'created_at' , 'updated_at' , 'created_by' , 'updated_by']