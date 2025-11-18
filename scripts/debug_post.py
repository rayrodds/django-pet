import os,sys, pathlib
project_root = str(pathlib.Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE','setup.settings')
import django
django.setup()
from django.test import Client
c=Client()
s=c.session
s['cadastro_step1']={'full_name':'Rayan Rodrigues','cpf_cnpj':'000','phone':'1','birth_date':'1990-01-01','gender':'m'}
s['cadastro_step2']={'cep':'000','city':'x','neighborhood':'y','street':'z','number':'1'}
s.save()
resp=c.post('/cadastro/step3/',{'email':'testuser@example.com','senha':'abc12345','senha2':'abc12345'},HTTP_HOST='127.0.0.1')
print('status',resp.status_code)
print(resp.content.decode('utf-8')[:2000])
