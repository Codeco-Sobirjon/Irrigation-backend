from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MainPartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.main_part'
    verbose_name = _("Основная часть")
