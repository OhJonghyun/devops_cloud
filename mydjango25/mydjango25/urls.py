from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from mydjango25 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]