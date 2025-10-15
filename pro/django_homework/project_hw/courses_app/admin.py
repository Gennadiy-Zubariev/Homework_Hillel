from django.contrib import admin
from courses_app.models import Courses


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'program']
    list_filter = ['title']
