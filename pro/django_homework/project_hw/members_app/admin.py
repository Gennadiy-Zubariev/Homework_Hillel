from django.contrib import admin
from members_app.models import Members


@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ['user_email', 'user_full_name', 'user_birth_date', 'courses_count']

    def user_email(self, obj):
        return obj.m_user.email

    user_email.short_description = 'Email'

    def user_full_name(self, obj):
        return obj.m_user.full_name or 'Не вказано'

    user_full_name.short_description = "Прізвище та ім'я"

    def user_birth_date(self, obj):
        return obj.m_user.date_of_birth or 'Не вказано'

    user_birth_date.short_description = 'Дата народження'

    def courses_count(self, obj):
        return obj.m_courses.count()

    courses_count.short_description = 'Кількість курсів'
