from django.utils import timezone
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserTestCase(APITestCase):
    def setUp(self):
        url = api_reverse('customers:users')
        data = {
            'username': 'user',
            'email': 'user@some.com',
            'password': 'some',
        }
        self.client.post(url, data, format='json')

    def test_create_users(self):
        url = api_reverse('customers:users')
        data = {
            'username': 'some',
            'email': 'some',
            'password': 'some',
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {
            'username': 'user',
            'email': 'user@some.com',
            'password': 'some',
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {
            'username': 'user2',
            'email': 'user@some.com',
            'password': 'some',
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_get_user(self):
        url = api_reverse('customers:users')
        data = {
            'username': 'some',
            'email': 'some@some.com',
            'password': 'some',
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        url = api_reverse('customers:user-detail', args=['some'])
        response = self.client.get(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        url = api_reverse('customers:user-detail', args=['some@some.com'])
        response = self.client.get(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)


class RentTestCase(APITestCase):
    def setUp(self):
        url = api_reverse('customers:users')
        data = {
            'username': 'user',
            'email': 'user@some.com',
            'password': 'some',
        }
        response = self.client.post(url, data, format='json')
        self.user = response.json()

        url = api_reverse('films:categories')
        data = {'name': 'movie'}
        response = self.client.post(url, data, format='json')
        movie = response.json()

        url = api_reverse('films:films')
        data = {
            'title': 'my mov',
            'description': 'just my mov',
            'stock': 20,
            'price': 35.5,
            'category': movie['id'],
            'release_date': timezone.now().date(),
        }
        response = self.client.post(url, data, format='json')
        self.my_mov = response.json()

    def test_rent_create(self):
        url = api_reverse('customers:rents')
        data = {
            'rented_at': '2021-11-11',
            'returned_at': '2021-11-12',
            'rented_days': 1,
            'film': self.my_mov['id'],
            'user': self.user['id'],
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        data = {
            'rented_at': '2021-11-11',
            'returned_at': '2021-11-10',
            'rented_days': 1,
            'film': self.my_mov['id'],
            'user': self.user['id'],
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
