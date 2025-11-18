import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
import sys
import pathlib
# ensure project root is on sys.path
project_root = str(pathlib.Path(__file__).resolve().parents[1])
if project_root not in sys.path:
	sys.path.insert(0, project_root)

import django
django.setup()
exec(open('scripts/fix_profiles.py').read())
