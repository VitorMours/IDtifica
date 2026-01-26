from django.apps import AppConfig

class ApiConfig(AppConfig):  # ← Mude de TestConfig para ApiConfig
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'