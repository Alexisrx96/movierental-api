# Generated by Django 3.2.9 on 2021-12-02 02:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('films', '0003_film_price__gte_one'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rented_at', models.DateField()),
                ('days_rented', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(15)])),
                ('returned_at', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, default=1.0, max_digits=5, validators=[django.core.validators.MinValueValidator(1)])),
                ('extra_day_fee', models.DecimalField(decimal_places=2, default=1.0, max_digits=5, validators=[django.core.validators.MinValueValidator(1)])),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rents', to='films.film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
