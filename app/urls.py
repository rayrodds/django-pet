from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="home"),
    path("download/", views.download, name="download"),
    path("parceiros/", views.parceiros, name="parceiros"),
    path("ajuda/", views.ajuda, name="ajuda"),
    path("sobre/", views.sobre, name="sobre"),
    path("login1pet/", views.login1pet, name="login1pet"),
    path("login/", views.login1pet, name="login"),  # rota usada pelos templates

    # rotas de cadastro
    path("cadastro/", views.cadastro, name="cadastro"),
    path("cadastro/step2/", views.cadastro2, name="cadastro2"),
    path("cadastro/step3/", views.cadastro3, name="cadastro3"),

    # esqueci senha
    path("esquecisenha1/", views.esquecisenha1, name="esquecisenha1"),
    path("esquecisenha2/", views.esquecisenha2, name="esquecisenha2"),
    path("esquecisenha3/", views.esquecisenha3, name="esquecisenha3"),

    # sucesso troca de senha
    path("senhatrocada/", views.senhatrocada, name="senhatrocada"),
]
