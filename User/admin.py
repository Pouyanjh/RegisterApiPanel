from django.contrib import admin
from .models import user
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'fullname', 'username', 'date_joined', 'is_staff']
    search_fields = ['username', 'email']
    readonly_fields = ['date_joined', 'last_login']
    filter_horizontal = ()
    list_filter = ('last_login',)
    fieldsets = []


    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields':('email', 'username', 'fullname', 'password1', 'password2'),
        })
    ),

admin.site.register(user, UserAdmin)
