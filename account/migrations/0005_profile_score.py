# Generated by Django 4.2.7 on 2024-02-05 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profile_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
