from django.utils import timezone
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SeasonTestCase(APITestCase):
    def setUp(self):
        url = api_reverse('films:categories')
        data = {'name': 'movie'}
        response = self.client.post(url, data, format='json')
        self.movie = response.json()

        data = {'name': 'serie'}
        response = self.client.post(url, data, format='json')
        self.serie = response.json()

        url = api_reverse('films:films')
        data = {
            'title': 'Futurama',
            'description': 'TV SERIE',
            'stock': 20,
            'price': 35.5,
            'category': self.serie['id'],
            'release_date': timezone.now().date(),
        }
        response = self.client.post(url, data, format='json')
        self.futurama = response.json()

        data = {
            'title': 'The Simpsons',
            'description': 'TV SERIE',
            'stock': 20,
            'price': 35.5,
            'category': self.serie['id'],
            'release_date': timezone.now().date(),
        }
        response = self.client.post(url, data, format='json')
        self.simpsons = response.json()

        data = {
            'title': 'A movie',
            'description': 'TV SERIE',
            'stock': 20,
            'price': 35.5,
            'category': self.movie['id'],
            'release_date': timezone.now().date(),
        }
        response = self.client.post(url, data, format='json')
        self.movie_film = response.json()

    def test_repeated_title(self):
        repeated_title = 'Season 1'
        url = api_reverse('films:seasons')
        data = {
            'title': repeated_title,
            'description': 'Season 1 futurama',
            'film': self.futurama['id'],
            'prequel': None,
            'sequel': None,
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        data = {
            'title': repeated_title,
            'description': 'Season 1 the simpsos',
            'film': self.simpsons['id'],
            'prequel': None,
            'sequel': None,
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        data = {
            'title': repeated_title,
            'description': 'Yep, again',
            'film': self.futurama['id'],
            'prequel': None,
            'sequel': None,
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_seasons_in_movies(self):
        url = api_reverse('films:seasons')
        data = {
            'title': 'Season 1',
            'description': 'Season 1 futurama',
            'film': self.movie_film['id'],
            'prequel': None,
            'sequel': None,
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)


class ChapterTestCase(APITestCase):
    def setUp(self):
        url = api_reverse('films:categories')
        data = {'name': 'serie'}
        response = self.client.post(url, data, format='json')
        self.serie = response.json()

        url = api_reverse('films:films')
        data = {
            'title': 'Futurama',
            'description': 'TV SERIE',
            'stock': 20,
            'price': 35.5,
            'category': self.serie['id'],
            'release_date': timezone.now().date(),
        }
        response = self.client.post(url, data, format='json')

        self.futurama = response.json()
        url = api_reverse('films:seasons')
        data = {
            'title': 'Season 1',
            'description': 'Season 1 futurama',
            'film': self.futurama['id'],
            'prequel': None,
            'sequel': None,
        }
        response = self.client.post(url, data, format='json')
        self.s1 = response.json()

        data = {
            'title': 'Season 2',
            'description': 'Season 2 futurama',
            'film': self.futurama['id'],
            'prequel': None,
            'sequel': None,
        }
        response = self.client.post(url, data, format='json')
        self.s2 = response.json()

    def test_repeated_chapters_titles(self):
        repeated_title = 'my title'
        url = api_reverse('films:chapters')
        data = {
            'title': repeated_title,
            'description': "Hey",
            'number': 1,
            'season': self.s1['id']
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        data = {
            'title': repeated_title,
            'description': "Hey",
            'number': 1,
            'season': self.s2['id']
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        data = {
            'title': repeated_title,
            'description': "Hey",
            'number': 2,
            'season': self.s1['id']
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_repeated_chapters_numbers(self):
        repeated_number = 1
        non_repeated_number = 2
        url = api_reverse('films:chapters')
        data = {
            'title': 'Chapter 1',
            'description': "Hey",
            'number': repeated_number,
            'season': self.s1['id']
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        data = {
            'title': 'Chapter 1',
            'description': "Hey",
            'number': repeated_number,
            'season': self.s2['id']
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        data = {
            'title': 'Chapter 1 (again)',
            'description': "Hey",
            'number': repeated_number,
            'season': self.s1['id']
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {
            'title': 'Chapter 2',
            'description': "Hey",
            'number': non_repeated_number,
            'season': self.s1['id']
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
