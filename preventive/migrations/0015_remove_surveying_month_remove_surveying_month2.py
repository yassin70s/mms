# Generated by Django 4.2.4 on 2023-08-29 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preventive', '0014_surveying_month2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveying',
            name='month',
        ),
        migrations.RemoveField(
            model_name='surveying',
            name='month2',
        ),
    ]
