from django.contrib import admin

from django200.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
     list_display = ('id', 'name', 'priority')
