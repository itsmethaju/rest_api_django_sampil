from rest_framework import fields, serializers
from rest_framework.utils import field_mapping
from .models import *
from django.contrib.auth import get_user_model

class userserializers(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    def create(self,validated_data):
        user=get_user_model().objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model=get_user_model()
        fields=['username','passerod']
class task_serializers(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    class Meta :
        model=Task
        fields=['id','Task_name','Task_desc','date_created','completed','image',]
