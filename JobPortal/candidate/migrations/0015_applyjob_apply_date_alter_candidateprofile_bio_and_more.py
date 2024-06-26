# Generated by Django 5.0.3 on 2024-03-27 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0014_candidateprofile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyjob',
            name='apply_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidateprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='candidateprofile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
