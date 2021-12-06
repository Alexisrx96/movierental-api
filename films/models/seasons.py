from django.db import models

from films.models.films import Film


class Season(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name='seasons'
    )
    prequel = models.ForeignKey(
        'self',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name='sequel_movie',
    )
    sequel = models.ForeignKey(
        'self',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )

    class Meta:
        unique_together = [['film', 'title']]

    def __str__(self) -> str:
        return self.title


class Chapter(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    number = models.PositiveIntegerField()
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        related_name='chapters',
    )

    class Meta:
        unique_together = [['season', 'number'], ['season', 'title']]

    def __str__(self) -> str:
        return (f"{self.season.film}, "
                f"Season: {self.season}, Chapter: {self.title}")
