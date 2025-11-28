from rest_framework import serializers
from courses_app.models import Courses
from teachers_app.models import Teacher
from members_app.models import Members
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name']


class TeacherSerializer(serializers.ModelSerializer):
    t_user = UserSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = ['full_teacher_name', 'bio', 'specialties', 't_user']


class CourseMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'title']


class MembersSerializer(serializers.ModelSerializer):
    m_user = UserSerializer(read_only=True)
    m_courses = CourseMiniSerializer(many=True, read_only=True)
    m_courses_id = serializers.PrimaryKeyRelatedField(queryset=Courses.objects.all(), source='m_courses',
                                                      write_only=True, required=False, many=True)

    class Meta:
        model = Members
        fields = ['m_user', 'm_courses', 'm_courses_id']


class MembersMiniSerializer(serializers.ModelSerializer):
    m_user = UserSerializer(read_only=True)

    class Meta:
        model = Members
        fields = ['m_user']


class CoursesSerializer(serializers.ModelSerializer):
    c_owner = UserSerializer(read_only=True)
    c_teachers = TeacherSerializer(many=True, read_only=True)
    c_teachers_id = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), source='c_teachers',
                                                       write_only=True, required=False, many=True)
    c_members = MembersMiniSerializer(source='rn_members', many=True, read_only=True)

    start_date = serializers.DateField(format='%d.%m.%Y')
    end_date = serializers.DateField(format='%d.%m.%Y')

    def validate(self, data):
        start = data.get('start_date')
        end = data.get('end_date')
        if start and end and end < start:
            raise serializers.ValidationError("Дата повинна бути раніше дати початку!")
        if start and start < date.today():
            raise serializers.ValidationError("Дата початку не може бути у минулому!")
        return data

    class Meta:
        model = Courses
        fields = ['id', 'title', 'start_date', 'end_date', 'c_teachers', 'c_teachers_id', 'c_owner', 'c_members']
