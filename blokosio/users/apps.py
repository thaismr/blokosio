from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "blokosio.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import blokosio.users.signals
        except ImportError:
            pass
