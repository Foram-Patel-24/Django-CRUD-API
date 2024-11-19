from rest_framework import serializers
from Category.models import Category

class CtgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name' , 'posts' , 'created_at' , 'updated_at' , 'created_by' , 'updated_by']