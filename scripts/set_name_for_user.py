import os, sys, pathlib
project_root = str(pathlib.Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
import django
django.setup()
from django.contrib.auth.models import User
from app.models import Profile

username = 'sosilvana1@outlook.com'
new_full = 'Rayan Rodrigues'

try:
    u = User.objects.get(username=username)
except User.DoesNotExist:
    print('User not found:', username)
    raise SystemExit(1)

p, created = Profile.objects.get_or_create(user=u)
p.full_name = new_full
p.save()
parts = new_full.split()
u.first_name = parts[0]
u.last_name = ' '.join(parts[1:]) if len(parts) > 1 else ''
u.save()
print('Updated user', username, '->', new_full)
