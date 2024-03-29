# Generated by Django 4.2.7 on 2024-02-03 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Moderate', 'Moderate'), ('Difficult', 'Difficult'), ('Professional', 'Professional')], max_length=225, null=True)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.quizcategory')),
            ],
        ),
    ]
