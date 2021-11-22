"""big_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url, include
from rest_framework import routers

from _notes.views import *
from _users.views import *

router = routers.DefaultRouter()
router.register('_users', UserViewSet)
router.register('_groups', GroupViewSet)
router.register('_notes', NotesViewSet)

urlpatterns = [
    url('^', include(router.urls)),
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
