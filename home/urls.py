from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from home.views import homeView, userView


urlpatterns = [
    url(r'^$', homeView),
    url(r'^home/$', homeView),
    url(r'^home/user/$', userView),


]
