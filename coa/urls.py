
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from coa.views import coa_home, add_coa


urlpatterns = [
    url(r'^$', coa_home),
    url(r'^coa/$', coa_home),
    url(r'^add_coa/$', add_coa)

]