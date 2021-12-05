from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase
from django.utils import timezone

from casts.models import CastMember, CastRole
from films.models import Category, Chapter, Film, FilmCast, Season


class FilmTestCase(TestCase):
    def setUp(self):
        movie = Category.objects.create(name="movie")

        self.my_mov = Film.objects.create(
            title='my mov',
            description="Just my mov",
            stock=60,
            price=35.5,
            category=movie,
            release_date=timezone.now(),
        )

    def test_film_availability(self):
        self.assertEquals(self.my_mov.availability, "Available")

        self.my_mov.stock = 0
        self.assertEquals(self.my_mov.availability, 'Out-of-Stocks')

    def test_film_wrong_price(self):
        self.my_mov.price = 0
        with self.assertRaises(ValidationError):
            self.my_mov.full_clean()

    def test_film_wrong_release_date(self):
        self.my_mov.release_date = timezone.now() + timezone.timedelta(days=1)
        with self.assertRaises(ValidationError):
            self.my_mov.full_clean()

    def test_film_correct_release_date(self):
        film = Film(
            title='a mov',
            description="Just my mov",
            stock=60,
            price=35.5,
            category=Category.objects.get(name="movie"),
            release_date=timezone.now() - timezone.timedelta(days=1),
        )
        film.full_clean()


class FilmCastTestCase(TestCase):
    def setUp(self):
        self.juan = CastMember.objects.create(
            name="Juan Valdez", birth_date="1990-11-21")
        self.carlos = CastMember.objects.create(
            name="Carlos Slim", birth_date="1990-11-21")

        self.actor = CastRole.objects.create(name='actor')
        self.director = CastRole.objects.create(name='director')

        movie = Category.objects.create(name="movie")

        self.my_mov = Film.objects.create(
            title='my mov',
            description="Just my mov",
            stock=60,
            price=35.5,
            category=movie,
            release_date=timezone.now(),
        )

    def test_add_film_cast(self):
        film_cast1 = FilmCast(
            movie=self.my_mov, cast=self.juan, role=self.actor)
        film_cast2 = FilmCast(
            movie=self.my_mov, cast=self.carlos, role=self.actor)
        film_cast3 = FilmCast(
            movie=self.my_mov, cast=self.carlos, role=self.director)
        film_cast4 = FilmCast(
            movie=self.my_mov, cast=self.carlos, role=self.director)
        film_cast1.save()
        film_cast2.save()
        film_cast3.save()
        with self.assertRaises(IntegrityError):
            film_cast4.save()


class SeasonTestCase(TestCase):
    def setUp(self):
        self.title = 'Season 1'
        Category.objects.create(name="movie")

        self.film = Film.objects.create(
            title='my mov',
            description="Just my mov",
            stock=60,
            price=35.5,
            category=Category.objects.get(name="movie"),
            release_date=timezone.now(),
        )

        self.film2 = Film.objects.create(
            title='another movie',
            description="Yeah! A new movie!",
            stock=1,
            price=40,
            category=Category.objects.get(name="movie"),
            release_date=timezone.now(),
        )
        Season.objects.create(
            title=self.title,
            description='s1',
            film=self.film
        )

    def test_chapter_add(self):
        s2 = Season(
            title='some title',
            description='an example',
            film=self.film
        )
        non_repeated = Season(
            title=self.title,
            description='repeated',
            film=self.film2
        )
        repeated = Season(
            title=self.title,
            description='repeated',
            film=self.film
        )
        s2.save()
        non_repeated.save()
        with self.assertRaises(IntegrityError):
            repeated.save()


class ChapterTestCase(TestCase):
    def setUp(self):
        self.title = "Starting"
        self.another_title = "Hello!"
        self.number = 1

        self.serie = Category.objects.create(name="serie")

        self.futurama = Film.objects.create(
            title='Futurama',
            description="On fox!!",
            stock=60,
            price=35.5,
            category=self.serie,
            release_date=timezone.now(),
        )

        self.season_f1 = Season.objects.create(
            title='Season 1',
            description='s1',
            film=self.futurama
        )

        self.season_f2 = Season.objects.create(
            title='Season 2',
            description='s2',
            film=self.futurama
        )

    def test_repeated_chapters_titles(self):
        chapter_f1 = Chapter(
            title=self.title,
            description="Hey",
            number=self.number,
            season=self.season_f1
        )
        chapter_f2 = Chapter(
            title=self.another_title,
            description="Hey",
            number=self.number+1,
            season=self.season_f1
        )
        chapter_f3 = Chapter(
            title=self.title,
            description="Hey",
            number=self.number+1,
            season=self.season_f1
        )
        chapter_f4 = Chapter(
            title=self.title,
            description="Hey",
            number=self.number,
            season=self.season_f2
        )
        chapter_f1.save()
        chapter_f2.save()
        chapter_f4.save()

        with self.assertRaises(IntegrityError):
            chapter_f3.save()

    def test_repeated_chapters_numbers(self):
        chapter_f1 = Chapter(
            title=self.title,
            description="Hey",
            number=self.number,
            season=self.season_f1
        )
        chapter_f2 = Chapter(
            title=self.another_title,
            description="Hey",
            number=self.number+1,
            season=self.season_f1
        )
        chapter_f3 = Chapter(
            title=self.another_title,
            description="Hey",
            number=self.number+1,
            season=self.season_f1
        )
        chapter_f4 = Chapter(
            title=self.title,
            description="Hey",
            number=self.number,
            season=self.season_f2
        )
        chapter_f1.save()
        chapter_f2.save()
        chapter_f4.save()

        # with same number
        with self.assertRaises(IntegrityError):
            chapter_f3.save()
