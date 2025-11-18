from django.contrib.auth.models import User
from app.models import Profile

updated = 0
updated_details = []

for u in User.objects.all():
    # get or create profile
    p, created = Profile.objects.get_or_create(user=u)
    fullname = (p.full_name or '').strip()
    user_has_name = bool((u.first_name or '').strip() or (u.last_name or '').strip())

    if not fullname and user_has_name:
        # copy from User to Profile
        p.full_name = ((u.first_name or '').strip() + (' ' + (u.last_name or '').strip() if (u.last_name or '').strip() else '')).strip()
        p.save()
        updated += 1
        updated_details.append(f"Profile updated from User for {u.username}: {p.full_name}")
    elif fullname and not user_has_name:
        # copy from Profile to User
        parts = fullname.split()
        u.first_name = parts[0]
        u.last_name = ' '.join(parts[1:]) if len(parts) > 1 else ''
        u.save()
        updated += 1
        updated_details.append(f"User updated from Profile for {u.username}: {u.first_name} {u.last_name}")

print('Total records updated:', updated)
for d in updated_details:
    print(d)
