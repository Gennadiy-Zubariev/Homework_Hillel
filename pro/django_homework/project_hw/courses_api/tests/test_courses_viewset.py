import pytest
from django.urls import reverse
from courses_api.tests.factories import CoursesFactory, MembersUserFactory, TeacherFactory
from datetime import date, timedelta
from courses_app.models import Courses
from django.test import RequestFactory
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db

class TestCoursesList:
    def test_list_return_only_current_user_courses(self):
        client = APIClient()
        user = MembersUserFactory()
        user_courses = CoursesFactory.create_batch(3, c_owner=user)
        client.force_authenticate(user=user)
        url = reverse('courses-list')
        response = client.get(url)

        assert response.status_code == 200
        ids = {item['id'] for item in response.data}
        assert ids == {course.id for course in user_courses}

class TestCoursesCreate:
    def test_create_sets_owner_ignores_payload_owner(self):
        client = APIClient()
        user = MembersUserFactory()
        other_user = MembersUserFactory()
        teacher_1 = TeacherFactory(t_user=user)
        teacher_2 = TeacherFactory(t_user=user)

        client.force_authenticate(user=user)
        url = reverse('courses-list')
        payload = {
            'title': 'My DRF course',
            'start_date': date.today() + timedelta(days=1),
            'end_date': date.today() + timedelta(days=365),
            'c_teachers_id': [teacher_1.id, teacher_2.id],
            'c_owner': other_user,

        }
        response = client.post(url, payload)

        assert response.status_code == 201, response.data
        assert response.data['c_owner']['id'] == user.id
        assert {teacher['full_teacher_name'] for teacher in response.data['c_teachers']} == {teacher_1.full_teacher_name, teacher_2.full_teacher_name}







