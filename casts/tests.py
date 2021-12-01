from django.db.utils import IntegrityError
from django.test import TestCase
from django.utils import timezone

from .models import Cast


class CastTestCase(TestCase):
    def test_cast_birth_day(self):
        tomorrow = timezone.now() + timezone.timedelta(days=1)
        yesterday = timezone.now() - timezone.timedelta(days=1)
        sarah = Cast(
            name="Juan Perez",
            birth_date=yesterday
        )
        john = Cast(
            name="John Connor",
            birth_date=tomorrow
        )
        sarah.save()
        with self.assertRaises(IntegrityError):
            john.save()