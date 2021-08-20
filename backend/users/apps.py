from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'username', 'first_name',)
    list_filter = ('email', 'username', 'first_name', 'is_active', 'is_staff', 'is_social_login', 'birth_day', 'created', 'updated')
    ordering = ('-created',)
    list_display = ('email', 'username', 'first_name', 'birth_day', 'is_active', 'is_staff', 'is_social_login')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_social_login')}),
        ('Personal', {'fields': ('birth_day',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(User, UserAdminConfig)