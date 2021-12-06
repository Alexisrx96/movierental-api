from django.utils import timezone
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserTestCase(APITestCase):
    def setUp(self):
        url = api_reverse('public:create')
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
            'stock': 1,
            'price': 5.5,
            'category': movie['id'],
            'release_date': timezone.now().date(),
        }
        response = self.client.post(url, data, format='json')
        self.my_mov = response.json()

    def test_rent_films(self):
        url = api_reverse('public:rent')
        data = {
            'rented_at': '2021-11-11',
            'rented_days': 1,
            'film': self.my_mov['id'],
            'user': self.user['id'],
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        rent = response.json()

        data = {
            'rented_at': '2021-11-12',
            'rented_days': 1,
            'film': self.my_mov['id'],
            'user': self.user['id'],
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

        url = api_reverse('public:return', args=[rent['id']])
        data = {
            'returned_at': '2021-11-15',
        }
        response = self.client.put(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        data = {
            'returned_at': '2021-11-14',
        }
        response = self.client.put(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

        url = api_reverse('films:film-details', args=[self.my_mov['id']])
        response = self.client.get(url, format='json')
        self.assertEquals(response.json()['stock'], 1)
