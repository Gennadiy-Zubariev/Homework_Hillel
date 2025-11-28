import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from courses_api.tests.factories import MembersUserFactory, CoursesFactory
from members_app.models import Members

pytestmark = pytest.mark.django_db

class TestMembersUpdate:
    def test_update_m_courses_via_ids(self):
        client = APIClient()
        user = MembersUserFactory()
        client.force_authenticate(user=user)

        member = Members.objects.create(m_user=user)
        course_1 = CoursesFactory(c_owner=user)
        course_2 = CoursesFactory(c_owner=user)

        url = reverse('members-detail', args=[member.pk])
        response = client.patch(url, {'m_courses_id': [course_1.id, course_2.id]})
        assert response.status_code == 200, response.data
        returned_titles = {course['title'] for course in response.data['m_courses']}
        assert returned_titles == {course_1.title, course_2.title}
