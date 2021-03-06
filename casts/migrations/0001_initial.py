# Generated by Django 3.2.9 on 2021-11-26 06:55

import django.db.models.functions.datetime
from django.db import migrations, models

import casts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('birth_date', models.DateField(validators=[casts.models.validate_date_not_in_future])),
            ],
        ),
        migrations.CreateModel(
            name='CastRole',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='cast',
            constraint=models.CheckConstraint(check=models.Q(('birth_date__lte', django.db.models.functions.datetime.Now())), name='birth_date_cannot_be_future_dated'),
        ),
    ]
