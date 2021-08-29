from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (("User", {"fields": ("is_publisher",)}),) + tuple(
        BaseUserAdmin.fieldsets
    )
    list_display = BaseUserAdmin.list_display + ("is_publisher",)

    #: Should not be changed directly, but only from registration form / project creation form
    readonly_fields = ("is_publisher",)
