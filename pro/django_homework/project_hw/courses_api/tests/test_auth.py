import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from courses_api.tests.factories import MembersUserFactory

pytestmark = pytest.mark.django_db

class TestAuth:
    def test_obtain_token_success(self):
        client = APIClient()
        password = '0000'
        user = MembersUserFactory()
        user.set_password(password)
        user.save()

        url = reverse('courses-token-obtain')
        response = client.post(url, {'email': user.email, 'password': password}, format='json')
        assert response.status_code == 200
        assert 'access' in response.data or 'token' in response.data or 'refresh' in response.data

    def test_obtain_token_invalid_credentials(self):
        client = APIClient()
        url = reverse('courses-token-obtain')
        response = client.post(url, {'email': 'no@ucer.com', 'password': '8888'}, format='json')
        assert response.status_code == 401

    def test_refresh_token_success(self):
        client = APIClient()
        password = '0000'
        user = MembersUserFactory()
        user.set_password(password)
        user.save()
        obtain_url = reverse('courses-token-obtain')
        obtain = client.post(obtain_url, {'email': user.email, 'password': password}, format='json')
        assert obtain.status_code == 200, obtain.data
        refresh = obtain.data.get('refresh')
        assert refresh
        refresh_url = reverse('courses-token-refresh')
        response = client.post(refresh_url, {'refresh': refresh}, format='json')
        assert response.status_code == 200, response.data
        assert response.data.get('access')

    def test_refresh_invalid_token(self):
        client = APIClient()
        refresh_url = reverse('courses-token-refresh')
        invalid_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.invalid.invalid'
        response = client.post(refresh_url, {'refresh': invalid_token}, format='json')
        assert response.status_code == 401






