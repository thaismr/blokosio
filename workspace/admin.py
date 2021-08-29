from django.contrib import admin
from .models import Workspace, WorkspaceMembers


@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    autocomplete_fields = ('owner',)
    search_fields = ('owner',)  # Manager available for list search and all around auto-completes


@admin.register(WorkspaceMembers)
class WorkspaceMembersAdmin(admin.ModelAdmin):
    autocomplete_fields = ('member', 'workspace')
