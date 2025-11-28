import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from courses_api.tests.factories import MembersUserFactory, TeacherFactory

pytestmark = pytest.mark.django_db

class TestTeacherList:
    def test_list_return_only_current_user_teachers(self):
        client = APIClient()
        user = MembersUserFactory()
        other_user = MembersUserFactory()
        user_teacher = TeacherFactory(t_user=user)
        other_user_teacher = TeacherFactory(t_user=other_user)
        client.force_authenticate(user=user)
        url = reverse('teacher-list')
        response = client.get(url)
        assert response.status_code == 200
        names = {teacher['full_teacher_name'] for teacher in response.data}
        assert names == {user_teacher.full_teacher_name}
