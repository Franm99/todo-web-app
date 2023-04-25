from django.apps import AppConfig


class TodoAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "todo_app"
    
    def ready(self):
        from todo_app.signals.handlers import get_state_from_date        
