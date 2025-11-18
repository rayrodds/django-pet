from .models import Profile


def user_display_name(request):
    """Return a display_name (first two words of full name) for templates."""
    user = getattr(request, 'user', None)
    display_name = ''
    if user and user.is_authenticated:
        full = ''
        try:
            profile = Profile.objects.filter(user=user).first()
            if profile:
                full = (profile.full_name or '').strip()
        except Exception:
            full = ''

        if not full:
            full = (user.get_full_name() or '').strip()

        if full:
            parts = full.split()
            display_name = ' '.join(parts[:2])
        else:
            username = user.username or ''
            display_name = username.split('@')[0] if '@' in username else username

    return {'display_name': display_name}
