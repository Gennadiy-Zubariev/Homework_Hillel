from django.apps import AppConfig


class AppActionLogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'action_logs_app'

    def ready(self):
        import action_logs_app.signals