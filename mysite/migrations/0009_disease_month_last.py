# Generated by Django 4.1.5 on 2023-02-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_categoriedisease_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='month_last',
            field=models.IntegerField(blank=True, max_length=7, null=True),
        ),
    ]