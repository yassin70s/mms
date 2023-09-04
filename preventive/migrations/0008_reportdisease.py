# Generated by Django 4.1.5 on 2023-01-31 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_report'),
        ('preventive', '0007_alter_report_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportDisease',
            fields=[
            ],
            options={
                'verbose_name': 'تقرير',
                'verbose_name_plural': 'تقارير',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('mysite.disease',),
        ),
    ]