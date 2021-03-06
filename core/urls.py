from django.conf.urls import url, include
from django.contrib import admin
from core import views


urlpatterns = [
    url(r'^$', views.index, name='index_view'),
    url(r'^contacts/$', views.contact_information, name='contact_information_view'),
    url(r'^calendar_events/$', views.calendar_events, name='calendar_events'),
    url(r'^video/$', views.video_list, name='video_list_view'),
    url(r'^photo/albums/$', views.photo_album_list, name='photo_album_list_view'),
    url(r'^photo/albums/(?P<pk>[-\d]+)/$', views.photo_album_detail, name='photo_album_detail_view'),
    url(r'^notes/$', views.note_list, name='note_list_view'),
    url(r'^formations/$', views.formation_list, name='formation_list_view'),
    url(r'^notes/(?P<pk>[-\d]+)/$', views.note_detail, name='note_detail_view'),
    url(r'^formation/(?P<pk>[-\d]+)/$', views.formation_detail, name='formation_detail_view'),
]
