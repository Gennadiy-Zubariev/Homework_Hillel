from rest_framework import serializers
from courses_app.models import Courses
from teachers_app.models import Teacher
from members_app.models import Members
from django.contrib.auth import get_user_model

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
                                                      write_only=True, required=False)

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

    class Meta:
        model = Courses
        fields = ['id', 'title', 'start_date', 'end_date', 'c_teachers', 'c_teachers_id', 'c_owner', 'c_members']
