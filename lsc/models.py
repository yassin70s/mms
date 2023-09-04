from django.db import models

# Create your models here.
class Setting(models.Model):
    active = models.BooleanField(("مفعل"),default=False)
    time = models.TimeField(("وقت البدء"), auto_now=False, auto_now_add=False)
    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

class Reports(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE)
    phone_name = models.CharField(("اسم المسؤول"), max_length=50)
    phone_number = models.BigIntegerField(("رقم الهاتف"))
    report_day = models.BooleanField(("التقرير اليومي"),default=False)
    report_wik = models.BooleanField(("التقرير الاسبوعي"),default=False)
    class Meta:
        verbose_name = ("Reports")
        verbose_name_plural = ("Reports")

    def __str__(self):
        return self.phone_name

class OperaSms(models.Model):
    id_message = models.IntegerField(("id_me"))
    date_time = models.DateTimeField(("date_time"), auto_now=False, auto_now_add=False)
    class Meta:
        verbose_name = ("OperaSms")
        verbose_name_plural = ("OperaSmss")