# Generated by Django 4.2.1 on 2023-09-18 10:44

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainercard', '0002_alter_trainercard_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainercard',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=django.core.files.storage.FileSystemStorage(location='/media/profilepics')),
        ),
    ]
