from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static


# it only handles the admin site
# and if any url comes other than admin it sends to base.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('base.urls')),
    path('api/',include('base.api.urls'))
]
   
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
