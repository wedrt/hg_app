from django.apps import AppConfig


class HgAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hg_app'

    def ready(self):
        import hg_app.signals
