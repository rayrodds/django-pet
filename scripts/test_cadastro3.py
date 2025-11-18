import os, sys, pathlib
project_root = str(pathlib.Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
import django
django.setup()
from django.test import Client
from django.contrib.auth.models import User
c = Client()
# simulate session steps
session = c.session
session['cadastro_step1'] = {
    'full_name': 'Rayan Rodrigues',
    'cpf_cnpj': '00000000000',
    'phone': '123456',
    'birth_date': '1990-01-01',
    'gender': 'masculino',
}
session['cadastro_step2'] = {
    'cep': '00000-000',
    'city': 'Cidade',
    'neighborhood': 'Bairro',
    'street': 'Rua X',
    'number': '123'
}
session.save()

resp = c.post('/cadastro/step3/', {'email':'testuser@example.com','senha':'abc12345','senha2':'abc12345'}, HTTP_HOST='127.0.0.1')
print('status_code', resp.status_code)
print('redirect chain', resp.redirect_chain)
print('content snippet', resp.content[:500])
# ensure user created
try:
    u = User.objects.get(username='testuser@example.com')
    print('User created:', u.username, u.first_name, u.last_name)
except Exception as e:
    print('User not created:', e)
