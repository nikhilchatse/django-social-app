from django.apps import AppConfig


class ProfileConfig(AppConfig):
    default_auto_field='django.db.models.BigAutoField'
    name = 'profile_'

    def ready(self):
        import profile_.signals
