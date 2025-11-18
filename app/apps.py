from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        # import signals to connect handlers
        try:
            import app.signals  # noqa: F401
        except Exception:
            pass
