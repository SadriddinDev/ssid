from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.admin import UserAdmin
from main.models import *


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Custom fields'), {'fields': ('image', 'birthday', 'status')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'status')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'url_redirect', 'allowed_domain']
    search_fields = ['name', 'username']


@admin.register(ShareAction)
class ShareActionAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'user', 'company']
