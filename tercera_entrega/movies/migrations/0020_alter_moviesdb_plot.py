# Generated by Django 5.1.1 on 2024-10-31 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0019_alter_moviesdb_main_actor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesdb',
            name='plot',
            field=models.CharField(default='2 guys go really slow in their sports cars.', max_length=100),
        ),
    ]
