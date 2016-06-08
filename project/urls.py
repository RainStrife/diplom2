from django.conf.urls import url, include
from django.contrib import admin

import core.urls
from django.conf.urls.static import static

from project import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(core.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)