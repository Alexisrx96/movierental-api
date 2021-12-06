from django.utils import timezone
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CastTestCase(APITestCase):
    def test_cast_birth_day(self):
        url = api_reverse('casts:members')
        after = timezone.now() + timezone.timedelta(days=1)
        before = timezone.now() - timezone.timedelta(days=10)
        data = {
            'name': "Alex",
            'birth_date': after.date()
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {
            'name': "Alex",
            'birth_date': before.date()
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
