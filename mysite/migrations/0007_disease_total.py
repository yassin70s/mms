# Generated by Django 4.1.5 on 2023-02-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_disease_exempt'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='total',
            field=models.IntegerField(blank=True, max_length=7, null=True),
        ),
    ]