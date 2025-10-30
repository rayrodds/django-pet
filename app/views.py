from django.shortcuts import render

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
    return render(request, "html/login1pet.html")

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
