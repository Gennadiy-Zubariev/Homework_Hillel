from django.contrib import admin
from accounts_app.models import MembersUser

@admin.register(MembersUser)
class MembersUser(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'password']
    list_filter = ['first_name']
