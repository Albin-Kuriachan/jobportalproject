# Generated by Django 5.0.3 on 2024-03-24 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0009_rename_appdlyjob_applyjob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applyjob',
            name='cover_letter',
        ),
        migrations.RemoveField(
            model_name='applyjob',
            name='resume',
        ),
    ]
