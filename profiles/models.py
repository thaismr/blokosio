from django.utils.translation import gettext_lazy as _
from django.db.models import (
    Model, OneToOneField, ManyToManyField, CharField,
    URLField, DateField, CASCADE
)

#: attach functionality to events
from django.db.models.signals import post_save
from django.dispatch import receiver

#: custom user model
from django.contrib.auth import get_user_model
from django.conf import settings

#: avoid circular dependency
from django.apps import apps

User = get_user_model()


class BaseUserProfile(Model):
    """Base profile with common fields."""

    #: User pk as profile pk
    user = OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=CASCADE,
        related_name='user_profile',
    )
    bio = CharField(_("Bio"), max_length=30, blank=True)
    website = URLField(_("Website"), max_length=255, blank=True)
    birth_date = DateField(_("Birth date"), null=True, blank=True)

    @property
    def full_name(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.user.get_full_name() or str(self.user)


class ManagerProfile(BaseUserProfile):
    """
    Project manager profile specific fields.
    https://docs.djangoproject.com/en/3.2/topics/db/models/#multi-table-inheritance
    """
    pass


class MemberProfile(BaseUserProfile):
    """
    Team member profile specific fields.
    https://docs.djangoproject.com/en/3.2/topics/db/models/#multi-table-inheritance
    """
    #: avoid circular dependency
    Workspace = apps.get_model('workspace', 'Workspace', require_ready=False)

    #: Workspaces joined
    #: https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ManyToManyField.through_fields
    workspaces = ManyToManyField(
        Workspace,
        blank=True,
        through='workspace.WorkspaceMembers'
    )

    class Meta:
        #: Custom permissions for member profiles
        #: https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#custom-permissions
        permissions = [
            ("change_profile_status", "Can change the status of user profiles"),
        ]


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    """When saving User event signals, create profile for user."""
    if instance.is_publisher:
        #: Always saves a manager profile in case user becomes a project publisher
        ManagerProfile.objects.get_or_create(user=instance)
    elif created:
        #: Only if newly created user should we presume not being a publisher == joining as team member
        MemberProfile.objects.get_or_create(user=instance)
