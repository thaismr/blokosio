from django.contrib import admin
from .models import Workspace, WorkspaceMembers


class WorkspaceMembersInline(admin.TabularInline):
    model = WorkspaceMembers
    autocomplete_fields = ('member',)
    extra = 1


@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    model = Workspace
    autocomplete_fields = ('owner',)
    search_fields = ('owner',)  # Fields available for list search and all around auto-completes
    inlines = (WorkspaceMembersInline,)
