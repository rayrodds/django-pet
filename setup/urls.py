from django.contrib import admin
from django.urls import path, include #botando o include pra incluir
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path("",include("app.urls")), #incluindo as urls do app

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
