from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=Profile)
def sync_user_name_on_profile_save(sender, instance, created, **kwargs):
    """When a Profile is saved, update the linked User's first_name/last_name."""
    try:
        full = (instance.full_name or '').strip()
        if full:
            parts = full.split()
            user = instance.user
            changed = False
            if user.first_name != parts[0]:
                user.first_name = parts[0]
                changed = True
            last = ' '.join(parts[1:]) if len(parts) > 1 else ''
            if user.last_name != last:
                user.last_name = last
                changed = True
            if changed:
                user.save()
    except Exception:
        pass


@receiver(post_save, sender=User)
def create_profile_on_user_create(sender, instance, created, **kwargs):
    """Ensure a Profile exists for every User."""
    if created:
        try:
            Profile.objects.get_or_create(user=instance)
        except Exception:
            pass
