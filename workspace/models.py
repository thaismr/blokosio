import blank
from django.conf import settings
from django.db.models import (
    Model, ForeignKey, CharField, DateTimeField, CASCADE
)
#: avoid circular dependencies
from django.apps import apps


class Workspace(Model):
    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name='workspaces')
    name = CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name


class WorkspaceMembers(Model):
    #: avoid circular dependencies
    MemberProfile = apps.get_model('profiles', 'MemberProfile', require_ready=False)

    member = ForeignKey(MemberProfile, on_delete=CASCADE, related_name='workspace_members')
    workspace = ForeignKey(Workspace, on_delete=CASCADE, related_name='workspace_members')
    date_joined = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.member} - {self.workspace}'
