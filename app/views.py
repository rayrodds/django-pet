from django.shortcuts import render, redirect
from django.contrib import messages
from . import models

# Create your views here.
def inicio(request):
    return render(request, "html/web_pet.html")

def download(request):
    return render(request, "html/download.html")

def parceiros(request):
    return render(request, "html/parceiros.html")

def ajuda(request):
    return render(request, "html/ajuda.html")

def sobre(request):
    return render(request, "html/sobre.html")

def login1pet(request):
    if request.method == 'GET':
        return render(request, "html/login1pet.html")
    
    if request.method == 'POST':
        login_post = request.POST.get("email")
        password_post = request.POST.get("senha")

        if not all([login_post, password_post]):
            messages.error(request, 'Todos os campos são obrigatórios')
            return redirect('login1pet')

        try:
            tutor = models.Tutor.objects.get(email=login_post)
            if tutor.senha == password_post:
                request.session['tutor_id'] = tutor.id
                request.session['nome_tutor'] = tutor.nome_tutor
                request.session['tutor_logado'] = True

                messages.success(request, f'Bem-vindo(a), {tutor.nome_tutor}!')
                return redirect('home') 
            else:
                messages.error(request, 'Senha incorreta')
                return redirect('login1pet')
        except models.Tutor.DoesNotExist:
            messages.error(request, 'Erro ao encontrar usuário')
            return redirect('login1pet')

# NOVAS VIEWS (cadastro)
def cadastro(request):
    return render(request, "html/cadastro.html")

def cadastro2(request):
    return render(request, "html/cadastro2.html")

# ADICIONADA: etapa 3 do cadastro
def cadastro3(request):
    return render(request, "html/cadastro3.html")

def esquecisenha1(request):
    return render(request, "html/esquecisenha1.html")

def esquecisenha2(request):
    return render(request, "html/esquecisenha2.html")  

def esquecisenha3(request):
    return render(request, "html/esquecisenha3.html")

def senhatrocada(request):
    return render(request, "html/senhatrocada.html")
