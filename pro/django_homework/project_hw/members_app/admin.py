from django.contrib import admin
from members_app.models import Members


@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'birth_date']
