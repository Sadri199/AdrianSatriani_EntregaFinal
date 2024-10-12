# Generated by Django 5.1.1 on 2024-10-12 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('plot', models.CharField(max_length=50)),
                ('mainActor', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
