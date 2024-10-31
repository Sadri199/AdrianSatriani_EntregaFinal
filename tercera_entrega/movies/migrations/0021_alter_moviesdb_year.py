# Generated by Django 5.1.1 on 2024-10-31 18:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0020_alter_moviesdb_plot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesdb',
            name='year',
            field=models.IntegerField(default=1951, validators=[django.core.validators.MinValueValidator(1950, message='Year cannot go before 1950!'), django.core.validators.MaxValueValidator(2030, message='Year cannot go after 2030!')]),
        ),
    ]