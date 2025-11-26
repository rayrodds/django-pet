from django.urls import path
from django.urls import reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.login1pet, name="login1pet"),
    path("home/", views.inicio, name="home"),
    path("download/", views.download, name="download"),
    path("parceiros/", views.parceiros, name="parceiros"),
    path("ajuda/", views.ajuda, name="ajuda"),
    path("sobre/", views.sobre, name="sobre"),
    path("login/", views.login1pet, name="login"),  # rota usada pelos templates

    # rotas de cadastro
    path("cadastro/", views.cadastro, name="cadastro"),
    path("cadastro/step2/", views.cadastro2, name="cadastro2"),
    path("cadastro/step3/", views.cadastro3, name="cadastro3"),

    # página de usuário logado
    path("homelogada/", views.homelogada, name="homelogada"),
    # configurações do usuário
    path("configuracoes/", views.configuracoes, name="configuracoes"),

    # profile views
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='profile_edit'),

    # esqueci senha
    path("esquecisenha1/", views.esquecisenha1, name="esquecisenha1"),
    path("esquecisenha2/", views.esquecisenha2, name="esquecisenha2"),
    path("esquecisenha3/", views.esquecisenha3, name="esquecisenha3"),

        # Django built-in password reset flow (uses console email backend)
        path('password_reset/',
            auth_views.PasswordResetView.as_view(
               template_name='html/esquecisenha1.html',
               email_template_name='html/password_reset_email.html',
               subject_template_name='html/password_reset_subject.txt',
               success_url=reverse_lazy('password_reset_done')
            ),
            name='password_reset'),
        path('password_reset/done/',
            auth_views.PasswordResetDoneView.as_view(template_name='html/esquecisenha2.html'),
            name='password_reset_done'),
        path('reset/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(
               template_name='html/esquecisenha3.html',
               success_url=reverse_lazy('password_reset_complete')
            ),
            name='password_reset_confirm'),
        path('reset/done/',
            auth_views.PasswordResetCompleteView.as_view(template_name='html/senhatrocada.html'),
            name='password_reset_complete'),

    # sucesso troca de senha
    path("senhatrocada/", views.senhatrocada, name="senhatrocada"),
    path("logout/", views.logout_view, name="logout"),
]
