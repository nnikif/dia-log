"""dialog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework import routers
from main.views import IndexView, SubmitView
from restful import views
from django.views.generic.base import RedirectView

router = routers.DefaultRouter()
router.register(r'dialogues', views.DialogueViewSet)

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/d/1")),
    # Examples:
    # url(r'^$', 'dialog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^d/', IndexView.as_view()),
    url(r'^submit/', SubmitView.as_view(), name='submit-view'),
    ]