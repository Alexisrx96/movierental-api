from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.functions import Now
from django.utils import timezone
from django.utils.encoding import smart_text


def validate_date_not_in_future(value):
    if value > timezone.now().date():
        raise ValidationError('date is in the future')


class CastRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120, unique=True)

    def __str__(self) -> str:
        return smart_text(self.name)


class CastMember(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    birth_date = models.DateField(validators=[validate_date_not_in_future])

    class Meta:
        verbose_name = 'Cast member'
        verbose_name_plural = 'Cast members'

        constraints = [
            models.CheckConstraint(
                check=models.Q(birth_date__lte=Now()),
                name='birth_date_cannot_be_future_dated'
            )
        ]

    def __str__(self) -> str:
        return smart_text(self.name)
