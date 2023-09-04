# Generated by Django 4.2.4 on 2023-08-29 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_categoriedisease_month_last'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriedisease',
            options={'managed': True, 'verbose_name': 'فئة مرض', 'verbose_name_plural': 'فئات الأمراض'},
        ),
        migrations.AlterModelOptions(
            name='disease',
            options={'managed': True, 'verbose_name': 'مرض', 'verbose_name_plural': 'أمراض'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'managed': True, 'verbose_name': 'المرفق', 'verbose_name_plural': 'المرافق'},
        ),
        migrations.AlterModelOptions(
            name='month',
            options={'managed': True, 'verbose_name': 'شهر', 'verbose_name_plural': 'أشهر'},
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'managed': True, 'verbose_name': 'تقرير', 'verbose_name_plural': 'تقارير'},
        ),
        migrations.AlterModelOptions(
            name='typecadre',
            options={'managed': True, 'verbose_name': 'نوع الكادر', 'verbose_name_plural': 'أنواع الكوادر'},
        ),
        migrations.AlterModelOptions(
            name='typefacility',
            options={'managed': True, 'verbose_name': 'نوع المرفق', 'verbose_name_plural': 'أنواع المرافق'},
        ),
        migrations.AlterModelTable(
            name='categoriedisease',
            table='',
        ),
        migrations.AlterModelTable(
            name='disease',
            table='',
        ),
        migrations.AlterModelTable(
            name='facility',
            table='',
        ),
        migrations.AlterModelTable(
            name='month',
            table='',
        ),
        migrations.AlterModelTable(
            name='report',
            table='',
        ),
        migrations.AlterModelTable(
            name='typecadre',
            table='',
        ),
        migrations.AlterModelTable(
            name='typefacility',
            table='',
        ),
    ]
