from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_of_creation']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_time', 'deadline']
    list_editable = ['start_time', 'deadline']
    list_filter = ['tags']
    prepopulated_fields = {'slug': ('name',)}