# Generated by Django 5.1.1 on 2024-10-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extras',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to='pfpics'),
        ),
    ]