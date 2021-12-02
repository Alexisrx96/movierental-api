from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from django.utils import timezone
import os

from films.models import Film

User = get_user_model()
"""This could be in the database"""
MAX_RENT_DAYS: int = os.getenv('MAX_RENT_DAYS', 15)
EXTRA_DAY_FEE: float = os.getenv('EXTRA_DAY_FEE', 2.0)


class Rent(models.Model):
    id = models.BigAutoField(primary_key=True)
    rented_at = models.DateField(default=timezone.now)
    returned_at = models.DateField(null=True)
    rented_days = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(MAX_RENT_DAYS),
            MinValueValidator(1)
        ],
        default=1,
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        default=1.00,
        validators=[MinValueValidator(1)]
    )
    extra_day_fee = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        validators=[MinValueValidator(1)],
        default=EXTRA_DAY_FEE,
    )
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name='rents',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='rents',
    )

    @property
    def total(self):
        if not self.returned_at:
            return None

        timeframe = self.returned_at - self.rented_at
        extra_days = timeframe.days - self.days_rented
        if extra_days < 0:
            extra_days = 0
        return (
            self.days_rented * self.price +
            self.extra_day_fee * extra_days
        )
