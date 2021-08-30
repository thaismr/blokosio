from django.contrib import admin
from .models import MemberProfile, ManagerProfile


@admin.register(ManagerProfile)
class ManagerProfileAdmin(admin.ModelAdmin):
    autocomplete_fields = ('user',)


@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
    autocomplete_fields = ('user',)

    #: Allow autocomplete fields to be used in workspaces admin
    search_fields = ('workspaces__name',)

    list_display = ('user', 'bio', 'website', 'birth_date', 'show_workspaces')
    fieldsets = (
        (None, {
            'fields': (
                ('user',),
                ('birth_date',),
                ('bio',),
                ('website',),
            )
        }),
        ('Workspaces', {
            # 'classes': ('collapse',),
            'fields': (
                # ('workspaces',),
                # ('workspace_members',),
            ),
        }),
    )

    def get_queryset(self, request):
        """
        Extendido para buscar campos ManyToMany relacionados
        """
        return super().get_queryset(request).prefetch_related('workspaces',)

    @admin.display(description='Member Workspaces')
    def show_workspaces(self, obj):
        return ", ".join([workspace.name for workspace in obj.workspaces.all()])
