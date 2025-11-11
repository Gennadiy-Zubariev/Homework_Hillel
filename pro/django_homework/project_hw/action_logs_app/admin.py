from django.contrib import admin
from .models import ActionLog


@admin.register(ActionLog)
class ActionLogAdmin(admin.ModelAdmin):
    list_display = ['action_type', 'user', 'content_type', 'object_id', 'timestamp']
    list_filter = ['action_type', 'timestamp', 'content_type']
    search_fields = ['user__email', 'description']
