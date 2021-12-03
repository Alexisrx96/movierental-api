# Generated by Django 3.2.9 on 2021-12-03 01:11

import customers.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0002_auto_20211201_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='extra_day_fee',
            field=models.DecimalField(decimal_places=2, default=2.0, max_digits=5, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='rent',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='rent',
            name='rented_at',
            field=models.DateField(default=customers.models.today),
        ),
        migrations.AlterField(
            model_name='rent',
            name='user',
            field=models.ForeignKey(limit_choices_to={'is_staff': False}, on_delete=django.db.models.deletion.CASCADE, related_name='rents', to=settings.AUTH_USER_MODEL),
        ),
    ]
