# Generated by Django 4.1.5 on 2023-02-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_alter_categoriedisease_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='exempt',
            field=models.BooleanField(default=False, verbose_name='يحتاج تأكيد مخبري'),
        ),
    ]
