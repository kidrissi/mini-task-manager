from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'status', 'deadline', 'created_date','assigned_to')
    list_filter = ('priority', 'status')
    search_fields = ('priority', 'status')
