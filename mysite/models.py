from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=150,verbose_name="اسم المحور")
    
    def __str__(self):
        return self.name
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'المحور'
        verbose_name_plural = 'المحاور'

### أمراض
class CategorieDisease(models.Model):
    name = models.CharField(max_length=150,verbose_name="جميع الأمراض")
    total = models.IntegerField(max_length=7,null=True,blank=True)
    month_last = models.IntegerField(max_length=7,null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'فئة مرض'
        verbose_name_plural = 'فئات الأمراض'
class Disease(models.Model):
    categorie = models.ForeignKey(CategorieDisease,on_delete=models.CASCADE)
    name = models.CharField(max_length=150,verbose_name="إسم المرض")
    facility = models.IntegerField(max_length=5,null=True,blank=True)
    month = models.IntegerField(max_length=5,null=True,blank=True)
    exempt = models.BooleanField(default=False,verbose_name="يحتاج تأكيد مخبري")
    total = models.IntegerField(max_length=7,null=True,blank=True)
    month_last = models.IntegerField(max_length=7,null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'مرض'
        verbose_name_plural = 'أمراض'


