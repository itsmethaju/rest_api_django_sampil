from django.shortcuts import render
from . models import Task
from . serializers import task_serializers,userserializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
# Create your views here.
class Task_viewsets(viewsets.ModelViewSet):
    permission_classes=(IsAuthenticated,)
    queryset=Task.objects.all().order_by('-date_created')
    serializer_class=task_serializers

class duetaskviewset(viewsets.ModelViewSet):
    queryset=Task.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class=task_serializers

class createuserview(CreateAPIView):
    model=get_user_model()
    permission_classes=(AllowAny,)
    serializer_class=userserializers

class complatedtaskviewset(viewsets.ModelViewSet):
    queryset=Task.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class=task_serializers