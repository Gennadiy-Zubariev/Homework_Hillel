from django.contrib import admin
from courses_app.models import Courses


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'program', 'start_date', 'end_date', 'c_owner']
    list_filter = ['title']
