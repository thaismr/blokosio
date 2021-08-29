from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site
from django.db.models import (
    Model, OneToOneField, ManyToManyField, BooleanField, CharField,
    URLField, DateField, CASCADE
)
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Allow for updatable User models without breaking foreign relations.
    """

    #: Project publisher registered with Blokos?
    is_publisher = BooleanField(
        _("Project publisher"),
        default=False,
        help_text='Project publisher registered with Blokos?'
    )

    #: Sites this user has account registered
    sites = ManyToManyField(
        Site,
        default=settings.SITE_ID
    )
