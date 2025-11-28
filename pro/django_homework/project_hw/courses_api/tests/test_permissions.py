import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from courses_api.tests.factories import MembersUserFactory

pytestmark = pytest.mark.django_db

class TestPermissionsNotAuthenticated:
    def test_courses_list_requires_auth_not_auth_user(self):
        client = APIClient()
        url = reverse('courses-list')
        response = client.get(url)
        assert response.status_code in (401, 403)


class TestPermissionsAuthenticated:
    def test_courses_list_requires_auth_user(self):
        client = APIClient()
        user = MembersUserFactory()
        client.force_authenticate(user=user)
        url = reverse('courses-list')
        response = client.get(url)
        assert response.status_code == 200