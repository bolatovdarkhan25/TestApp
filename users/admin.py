from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BaseUser


class UsAdmin(UserAdmin):

    list_display = ('id', 'username', 'superuser',)
    list_filter = ('superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('superuser', 'staff', 'active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
         ),
    )

    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(BaseUser, UsAdmin)