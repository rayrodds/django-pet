import os, sys, pathlib
project_root = str(pathlib.Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
import django
django.setup()
from django.contrib.auth.models import User
from app.models import Profile

for u in User.objects.all():
    try:
        p = u.profile
        pname = p.full_name
    except Exception:
        pname = None
    print(f"username={u.username!r}, first={u.first_name!r}, last={u.last_name!r}, profile_full_name={pname!r}")
