from django.conf.urls import url
from . import views
from django.contrib import admin
from tution import views
from django.contrib.auth import views as auth_views
app_name = 'tution'

urlpatterns = [
             url(r'^$', views.index, name='index'),
             url(r'^signup/$', views.signup, name='signup'),

             url(r'^student/add/$', views.StudentCreate.as_view(), name='student-add'),


             url(r'^contact/$', views.contact, name='contact'),  ]