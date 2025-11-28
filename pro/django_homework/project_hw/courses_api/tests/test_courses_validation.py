import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from courses_api.tests.factories import MembersUserFactory
from datetime import date, timedelta

pytestmark = pytest.mark.django_db

class TestCoursesDates:
    def test_end_date_must_be_after_start_date(self):
        client = APIClient()
        user = MembersUserFactory()
        client.force_authenticate(user=user)

        url = reverse('courses-list')
        payload = {'title': 'My course', 'start_date': str(date.today()), 'end_date': str(date.today() - timedelta(days=1))}
        response = client.post(url, payload, format='json')
        assert response.status_code == 400

    def test_end_date_must_be_in_future(self):
        client = APIClient()
        user = MembersUserFactory()
        client.force_authenticate(user=user)

        url = reverse('courses-list')
        payload = {'title': 'My course', 'start_date': str(date.today() - timedelta(days=365)),
                   'end_date': str(date.today() - timedelta(days=1))}
        response = client.post(url, payload, format='json')
        assert response.status_code == 400


