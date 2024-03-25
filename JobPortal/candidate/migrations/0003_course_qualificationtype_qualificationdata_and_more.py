# Generated by Django 5.0.3 on 2024-03-24 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_candidateprofile_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='QualificationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='QualificationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_completed', models.DateField(blank=True, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidate.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.candidateprofile')),
                ('qualifiction_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidate.qualificationtype')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.qualificationtype'),
        ),
    ]
