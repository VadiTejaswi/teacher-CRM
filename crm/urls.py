
from django.contrib import admin
from django.urls import path,include
from . import views
# project/urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('',views.land),
    path('',include('Teacher.urls')),#app name
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

