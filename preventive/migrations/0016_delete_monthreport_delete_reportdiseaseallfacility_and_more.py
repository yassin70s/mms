# Generated by Django 4.2.4 on 2023-09-03 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preventive', '0015_remove_surveying_month_remove_surveying_month2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MonthReport',
        ),
        migrations.DeleteModel(
            name='ReportDiseaseAllFacility',
        ),
        migrations.RemoveField(
            model_name='surveying',
            name='cadre',
        ),
    ]
