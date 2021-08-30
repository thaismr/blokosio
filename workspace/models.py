from django.db.models import (
    Model, UniqueConstraint, ForeignKey, ManyToManyField, CharField, DateTimeField, BooleanField, CASCADE, SET_NULL
)
from django.conf import settings
from profiles.models import MemberProfile

#: avoid circular dependencies
from django.apps import apps


class Workspace(Model):
    owner = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=SET_NULL,
        blank=False,
        null=True,
        related_name='workspaces_owned',
        limit_choices_to={'is_staff': True}
    )
    name = CharField(null=False, blank=False, max_length=255)
    is_active = BooleanField(default=False)
    members = ManyToManyField(
        # 'profiles.MemberProfile',
        MemberProfile,
        #: ManyToManyField relations table
        through='WorkspaceMembers',
        #: fields for origin (this model) and target model
        through_fields=('workspace', 'member'),
        related_name='workspaces'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class WorkspaceMembers(Model):
    #: avoid circular dependencies
    # MemberProfile = apps.get_model('profiles', 'MemberProfile', require_ready=False)

    workspace = ForeignKey(Workspace, on_delete=CASCADE, related_name='joined_workspaces')
    member = ForeignKey(MemberProfile, on_delete=CASCADE, related_name='joined_workspaces')
    date_joined = DateTimeField(auto_now_add=True)

    class Meta:
        #: Make sure a member can't join the same workspace twice
        constraints = [
            UniqueConstraint(fields=['workspace', 'member'], name='unique_membership')
        ]

    def __str__(self):
        return f'{self.workspace} member: {self.member}'
