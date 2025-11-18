from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

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
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('homelogada')
        error = 'Credenciais inválidas'
    return render(request, "html/login1pet.html", {"error": error})

# NOVAS VIEWS (cadastro)
def cadastro(request):
    error = None
    if request.method == 'POST':
        # save step1 fields in session and go to step2
        request.session['cadastro_step1'] = {
            'full_name': request.POST.get('full_name', ''),
            'cpf_cnpj': request.POST.get('cpf_cnpj', ''),
            'phone': request.POST.get('phone', ''),
            'birth_date': request.POST.get('birth_date', ''),
            'gender': request.POST.get('gender', ''),
        }
        return redirect('cadastro2')
    return render(request, "html/cadastro.html", {'error': error})

def cadastro2(request):
    error = None
    if request.method == 'POST':
        request.session['cadastro_step2'] = {
            'cep': request.POST.get('cep', ''),
            'city': request.POST.get('city', ''),
            'neighborhood': request.POST.get('neighborhood', ''),
            'street': request.POST.get('street', ''),
            'number': request.POST.get('number', ''),
        }
        return redirect('cadastro3')
    return render(request, "html/cadastro2.html", {'error': error})

# ADICIONADA: etapa 3 do cadastro
def cadastro3(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')
        if not email or not senha or not senha2:
            error = 'Preencha todos os campos'
        elif senha != senha2:
            error = 'Senhas não conferem'
        elif User.objects.filter(username=email).exists():
            error = 'Usuário já existe'
        else:
            user = User.objects.create_user(username=email, email=email, password=senha)
            user.save()
            # create profile from session data
            step1 = request.session.get('cadastro_step1', {})
            step2 = request.session.get('cadastro_step2', {})
            # create or update profile (signals may have already created it)
            profile, created = Profile.objects.get_or_create(user=user)
            profile.full_name = step1.get('full_name', '')
            profile.cpf_cnpj = step1.get('cpf_cnpj', '')
            profile.phone = step1.get('phone', '')
            profile.birth_date = step1.get('birth_date') or None
            profile.gender = step1.get('gender', '')
            profile.cep = step2.get('cep', '')
            profile.city = step2.get('city', '')
            profile.neighborhood = step2.get('neighborhood', '')
            profile.street = step2.get('street', '')
            profile.number = step2.get('number', '')
            profile.save()
            # clear session steps
            request.session.pop('cadastro_step1', None)
            request.session.pop('cadastro_step2', None)
            # Also populate User.first_name and last_name from Profile.full_name
            try:
                full = (profile.full_name or '').strip()
                if full:
                    parts = full.split()
                    user.first_name = parts[0]
                    user.last_name = ' '.join(parts[1:]) if len(parts) > 1 else ''
                    user.save()
            except Exception:
                pass
            login(request, user)
            return redirect('homelogada')
    return render(request, "html/cadastro3.html", {"error": error})

def esquecisenha1(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            error = 'Informe o email'
        else:
            # salvar email na sessão e seguir para o código (sem envio real)
            request.session['reset_email'] = email
            return redirect('esquecisenha2')
    return render(request, "html/esquecisenha1.html", {"error": error})


def esquecisenha2(request):
    error = None
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        # para demo: aceitamos qualquer código e seguimos
        request.session['reset_code'] = codigo
        return redirect('esquecisenha3')
    return render(request, "html/esquecisenha2.html", {"error": error})


def esquecisenha3(request):
    error = None
    if request.method == 'POST':
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')
        email = request.session.get('reset_email')
        if not email:
            error = 'Email não informado. Reinicie o processo.'
        elif not senha or not senha2:
            error = 'Preencha as senhas'
        elif senha != senha2:
            error = 'Senhas não conferem'
        else:
            try:
                user = User.objects.get(username=email)
                user.set_password(senha)
                user.save()
            except User.DoesNotExist:
                # se não existir, opcionalmente criar
                user = User.objects.create_user(username=email, email=email, password=senha)
                user.save()
            # limpar sessão e redirecionar para sucesso
            request.session.pop('reset_email', None)
            request.session.pop('reset_code', None)
            return redirect('senhatrocada')
    return render(request, "html/esquecisenha3.html", {"error": error})

def senhatrocada(request):
    return render(request, "html/senhatrocada.html")


@login_required(login_url='login1pet')
def homelogada(request):
    # compute display name: prefer Profile.full_name (first two words),
    # fallback to User.get_full_name() or username prefix
    display_name = None
    try:
        profile = request.user.profile
        full = (profile.full_name or '').strip()
    except Exception:
        full = (request.user.get_full_name() or '').strip()

    if full:
        parts = full.split()
        display_name = ' '.join(parts[:2])
    else:
        # use username before @ if it's an email
        username = request.user.username or ''
        if '@' in username:
            display_name = username.split('@')[0]
        else:
            display_name = username

    return render(request, "html/homelogada.html", {'display_name': display_name})


@login_required(login_url='login1pet')
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'html/profile.html', {'profile': profile})


@login_required(login_url='login1pet')
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save()
            # update User.first_name/last_name from profile.full_name
            try:
                full = (profile.full_name or '').strip()
                if full:
                    parts = full.split()
                    request.user.first_name = parts[0]
                    request.user.last_name = ' '.join(parts[1:]) if len(parts) > 1 else ''
                    request.user.save()
            except Exception:
                pass
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'html/profile_edit.html', {'form': form})


@login_required(login_url='login1pet')
def configuracoes(request):
    # simple settings page — template already exists and displays user info
    return render(request, 'html/configuracoes.html')

def logout_view(request):
    logout(request)
    return redirect('home')
