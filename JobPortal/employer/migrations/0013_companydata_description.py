# Generated by Django 5.0.3 on 2024-03-30 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0012_jobdata_category_alter_jobdata_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydata',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
