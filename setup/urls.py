from django.contrib import admin
from django.urls import path, include #botando o include pra incluir

urlpatterns = [
    path('admin/', admin.site.urls), 
    path("",include("app.urls")), #incluindo as urls do app

]
