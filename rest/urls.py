"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from django.conf import settings
# import rest_framework
# from rest_framework.generics import CreateAPIView
from restapp .views import Task_viewsets,createuserview
from restapp import views
from django.conf.urls.static import static
# router=routers.DefaultRouter()
router=routers.SimpleRouter()
router.register('task',Task_viewsets)
router.register('due_task',views.duetaskviewset)
router.register('complated_task',views.complatedtaskviewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.createuserview.as_view(),name='user'),
    path('api_auth/',include('rest_framework.urls')),
    path('',include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

