# Generated by Django 5.0.3 on 2024-03-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0009_jobdata_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdata',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Any', 'any')], default='any', max_length=10, null=True),
        ),
    ]
