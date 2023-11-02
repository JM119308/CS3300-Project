from django.apps import AppConfig


class ScheduleAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedule_app'

class YourAppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedule_app'

    def ready(self):
        import schedule_app.signals  # Replace your_app_name with the name of your app
