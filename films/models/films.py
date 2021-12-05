from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.functions import Now
from django.utils.encoding import smart_text

from casts.models import CastMember, CastRole, validate_date_not_in_future


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return smart_text(self.name)


class Film(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(
        decimal_places=2, max_digits=5, default=1.00,
        validators=[MinValueValidator(1)])
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='films',
    )
    release_date = models.DateField(validators=[validate_date_not_in_future])
    roles = models.ManyToManyField(CastRole, through='FilmCast')
    casts = models.ManyToManyField(CastMember, through='FilmCast')

    @property
    def availability(self):
        return "Available" if self.stock > 0 else 'Out-of-Stocks'

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(release_date__lte=Now()),
                name='release_date_cannot_be_future_dated'
            ),
            models.CheckConstraint(
                check=models.Q(price__gte=1.0),
                name='price__gte_one'
            )
        ]

    def __str__(self) -> str:
        return smart_text(self.title)


class FilmCast(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    member = models.ForeignKey(CastMember, on_delete=models.CASCADE)
    role = models.ForeignKey(CastRole, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['film', 'member', 'role']]
        verbose_name = 'Cast'

    def __str__(self) -> str:
        return f"{self.role} on {self.film}"
