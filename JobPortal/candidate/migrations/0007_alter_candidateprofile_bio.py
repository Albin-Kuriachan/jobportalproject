# Generated by Django 5.0.3 on 2024-03-24 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0006_appdyjob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]