# Generated by Django 5.1.1 on 2024-10-26 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_alter_moviesdb_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesdb',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]