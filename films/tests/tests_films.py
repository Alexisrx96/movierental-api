from django.test import TestCase
from django.utils import timezone
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
from rest_framework.test import APITestCase


class FilmTestCase(APITestCase):
    def setUp(self):
        url = api_reverse('films:categories')
        data = {'name': 'movie'}
        response = self.client.post(url, data, format='json')
        self.movie = response.json()

        url = api_reverse('films:films')
        data = {
            'title': 'my mov',
            'description': 'just my mov',
            'stock': 20,
            'price': 35.5,
            'category': self.movie['id'],
            'release_date': timezone.now().date(),
        }
        response = self.client.post(url, data, format='json')
        self.my_mov = response.json()

    def test_film_availability(self):
        self.assertEquals(self.my_mov['availability'], "Available")
        self.my_mov['stock'] = 0

        url = api_reverse('films:film-detail', args=[self.my_mov['id']])
        response = self.client.put(url, self.my_mov, format='json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['availability'], 'Out-of-Stocks')

    def test_film_wrong_price(self):
        self.my_mov['price'] = 0
        url = api_reverse('films:film-detail', args=[self.my_mov['id']])
        response = self.client.put(url, self.my_mov, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_film_wrong_release_date(self):
        self.my_mov['release_date'] = (
            timezone.now() + timezone.timedelta(days=1)).date()
        url = api_reverse('films:film-detail', args=[self.my_mov['id']])
        response = self.client.put(url, self.my_mov, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)


class FilmCastTestCase(TestCase):
    def setUp(self):
        url = api_reverse('casts:members')
        data = {
            'name': "Juan Valdez",
            'birth_date': "1990-11-21",
        }
        response = self.client.post(url, data, format='json')
        self.juan = response.json()

        data = {
            'name': "Carlos Slim",
            'birth_date': "1990-11-21",
        }
        response = self.client.post(url, data, format='json')
        self.carlos = response.json()

        url = api_reverse('casts:roles')
        data = {'name': "actor"}
        response = self.client.post(url, data, format='json')
        self.actor = response.json()

        data = {'name': "director"}
        response = self.client.post(url, data, format='json')
        self.director = response.json()

        url = api_reverse('films:categories')
        data = {'name': "movie"}
        response = self.client.post(url, data, format='json')
        movie = response.json()

        url = api_reverse('films:films')
        data = {
            'title': 'my mov',
            'description': "Just my mov",
            'stock': 60,
            'price': 35.5,
            'category': movie['id'],
            'release_date': timezone.now().date(),
        }
        response = self.client.post(url, data, format='json')
        self.my_mov = response.json()

    def test_add_film_cast(self):
        url = api_reverse('films:filmcasts')
        data = {
            'film': self.my_mov['id'],
            'member': self.juan['id'],
            'role': self.actor['id'],
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        data = {
            'film': self.my_mov['id'],
            'member': self.carlos['id'],
            'role': self.actor['id'],
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        data = {
            'film': self.my_mov['id'],
            'member': self.carlos['id'],
            'role': self.director['id'],
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
