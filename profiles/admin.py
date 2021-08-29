from django.contrib import admin
from .models import MemberProfile, ManagerProfile


@admin.register(ManagerProfile)
class ManagerProfileAdmin(admin.ModelAdmin):
    autocomplete_fields = ('user',)


@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
    autocomplete_fields = ('user',)
    search_fields = ('workspaces',)
