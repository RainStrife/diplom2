from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'auth2.views.home'),
    url(r'^email-sent/', 'auth2.views.validation_sent'),
    url(r'^login/$', 'auth2.views.home'),
    url(r'^logout/$', 'auth2.views.logout'),
    url(r'^done/$', 'auth2.views.done', name='done'),
    url(r'^accounts/profile/$', 'auth2.views.done', name='done'),
    url(r'^ajax-auth/(?P<backend>[^/]+)/$', 'auth2.views.ajax_auth',
        name='ajax-auth'),
    url(r'^email/$', 'auth2.views.require_email', name='require_email'),

]
