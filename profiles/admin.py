from django.contrib import admin
from .models import MemberProfile, ManagerProfile


@admin.register(ManagerProfile)
class ManagerProfileAdmin(admin.ModelAdmin):
    autocomplete_fields = ('user',)


@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
    autocomplete_fields = ('user',)

    #: Allow autocomplete fields to be used in workspaces admin
    search_fields = ('workspaces',)

    list_display = ('user', 'bio', 'website', 'birth_date',)
    fieldsets = (
        (None, {
            'fields': (
                ('user',),
                ('birth_date',),
                ('bio',),
                ('website',),
            )
        }),
        ('Workspace', {
            # 'classes': ('collapse',),
            'fields': (
                # ('get_joined_workspaces',),
            ),
        }),
    )
