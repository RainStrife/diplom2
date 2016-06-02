from django.conf.urls import url, include
from django.contrib import admin
from core import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^notes/$', views.note_list, name='note_list_view'),
    url(r'^notes/(?P<pk>[-\d]+)/$', views.note_detail, name='note_detail_view'),
]
