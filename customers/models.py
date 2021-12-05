import os

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone

from films.models import Film

User = get_user_model()
"""This could be in the database"""
MAX_RENT_DAYS: int = int(os.getenv('MAX_RENT_DAYS', 15))
EXTRA_DAY_FEE: float = os.getenv('EXTRA_DAY_FEE', 2.0)


def today():
    return timezone.now().date()


class Rent(models.Model):
    id = models.BigAutoField(primary_key=True)
    rented_at = models.DateField(default=today)
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
        limit_choices_to={'is_staff': False}
    )

    @property
    def total(self):
        if not self.returned_at:
            return None

        timeframe = self.returned_at - self.rented_at
        extra_days = timeframe.days - self.rented_days
        if extra_days < 0:
            extra_days = 0
        return (
            self.rented_days * self.price +
            self.extra_day_fee * extra_days
        )


@receiver(pre_save, sender=Rent)
def pre_save_set_price(sender, instance: Rent, *args, **kwargs):
    if not instance.price:
        instance.price = instance.film.price

    if instance.id is None:
        pass
    else:
        previous = Rent.objects.get(id=instance.id)
        if instance.returned_at and not previous.returned_at:
            instance.film.stock = instance.film.stock + 1
            instance.film.save()


@receiver(post_save, sender=Rent)
def post_save_rent(sender, instance: Rent, created, *args, **kwargs):
    if created and not instance.returned_at:
        instance.film.stock = instance.film.stock - 1
        instance.film.save()
