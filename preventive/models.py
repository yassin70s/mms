from typing import Iterable, Optional
from django.db import models
from django.contrib import admin
from mysite.models import Facility,Disease,CategorieDisease

# Create your models here.
from django.utils.html import format_html
from django.shortcuts import get_object_or_404
import io
from django.http import FileResponse
REPORTS = [
            (1,"تقرير إحصائي للحالات المرضية في جميع معسكرات التدريب التابعة للمنطقة"),
            (2,"تقرير إحصاء تفصيلي للمعسكرات"),
        ]
from datetime import datetime
date = datetime
class Surveying(models.Model):
    '''Model definition for Surveying.'''
    facility = models.ForeignKey(Facility, verbose_name=("اسم المحور"), on_delete=models.CASCADE)
    
    date = models.DateField(("التاريخ"), auto_now=False, auto_now_add=False)
    message_id = models.IntegerField(max_length=8,blank=True,null=True)
    class Meta:
        '''Meta definition for Surveying.'''

        verbose_name = 'أوبئة'
        verbose_name_plural = 'الترصد الوبائي'
        

    def __str__(self):
        return str(self.facility)
    def save(self,*args, **kwargs):
        self.month2 = self.date.month
        return super().save(*args, **kwargs)
    

class SurveyingDisease(models.Model):
    
    Surveying = models.ForeignKey(Surveying, verbose_name=(""), on_delete=models.CASCADE)
    Disease = models.ForeignKey(Disease, verbose_name=("المرض"), on_delete=models.CASCADE)
    total = models.IntegerField(("العدد"),max_length=3)
    class Meta:
        verbose_name = 'مرض'
        verbose_name_plural = "الأمراض"
        


def dd(CategorieDisease_id,Facility_id):
      da = 0
      for f in Disease.objects.filter(categorie_id=CategorieDisease_id):
          for ff in SurveyingDisease.objects.filter(disaese_id=f.id).filter(Surveying__facility_id=Facility_id):
              da += ff.total
      return da


class Report(models.Model):
    
    name = models.IntegerField(("اسم التقرير"), max_length=150,null=True,blank=True)
    facility = models.IntegerField(max_length=5, verbose_name=("اسم المحور"),null=True,blank=True)
    
    month = models.IntegerField(("الشهر"),max_length=3,null=True,blank=True)
    
    class Meta:
        '''Meta definition for MonthReport.'''
     
        verbose_name = 'تقرير'
        verbose_name_plural = 'تقارير'

    def __str__(self):
        return str(self.facility)
    
    def مؤكدة_مخبريا(self):
        re = ""
        m = 1
        for de in Disease.objects.filter(exempt=True):
            dd=0
            for sur in SurveyingDisease.objects.filter(Disease_id=de.id):
                s = Surveying.objects.get(id=sur.Surveying_id)
                if sur.Surveying_id == s.id and s.date.month == self.month:
                    dd += sur.total
            re+="""<div class="row border-bottom">
                                <div class="col-1 border-left p-1">
                                    {}
                                </div>
                                <div class="col-6 border-left p-1">
                                   {}
                                </div>
                                <div class="col-5 border-left">
                                    <div class="row">
                                        <div class="col-7 p-1">
                                            {}
                                        </div>
                                        <div class="col-5 border-left p-1">
                                            {}
                                        </div>
                                    </div>
                                </div>
                    </div>""".format(m,de.name," ",dd)
            m+=1
        return re

    def حالات_عامة(self):
        re = ""
        m = 1
        for de in Disease.objects.filter(exempt=False):
            if m <= 16:
                dd=0
                for sur in SurveyingDisease.objects.filter(Disease_id=de.id):
                    s = Surveying.objects.get(id=sur.Surveying_id)
                    if sur.Surveying_id == s.id and s.date.month == self.month:
                        dd += sur.total
                re+="""<div class="row border-bottom">
                                <div class="col-1 border-left p-1">
                                    {}
                                </div>
                                <div class="col-8 border-left p-1">
                                   {}
                                </div>
                                <div class="col-3 border-left p-1">
                                    {}
                                </div>
                            </div>""".format(m,de.name,dd)
            m+=1
        return re
    def حالات_عامة_2(self):
        re = ""
        m = 1
        for de in Disease.objects.filter(exempt=False):
            if m > 16:
                dd=0
                for sur in SurveyingDisease.objects.filter(Disease_id=de.id):
                    s = Surveying.objects.get(id=sur.Surveying_id)
                    if sur.Surveying_id == s.id and s.date.month == self.month:
                        dd += sur.total
                re+="""<div class="row border-bottom">
                                <div class="col-1 border-left p-1">
                                    {}
                                </div>
                                <div class="col-8 border-left p-1">
                                   {}
                                </div>
                                <div class="col-3 border-left p-1">
                                    {}
                                </div>
                            </div>""".format(m,de.name,dd)
            m+=1
        return re
    def اجمالي_الحالات(self):
        sum_die = 0
        for f in SurveyingDisease.objects.all():
            s = Surveying.objects.get(id=f.Surveying_id)
            if f.Surveying_id == s.id and s.date.month == self.month:
                sum_die += f.total
        return str(sum_die)
    def اجمالي_الحالات_التي_عولجت(self):
        sum_die = 0
        for f in SurveyingDisease.objects.all():
            s = Surveying.objects.get(id=f.Surveying_id)
            if f.Surveying_id == s.id and s.date.month == self.month:
                sum_die += f.total
        return str(sum_die)
    def الحالات_التي_حولت(self):
        re=""" <tr>
                                       
                                        <td>
                                           0 
                                        </td>
                                       <td>
                                           انا
                                        </td>
                                    </tr>"""
        return re
    def حالات_الوفاة(self):
        re="""
        """
        return re
    def الفرق(self):
        re = ""
        dis = Disease.objects.all()
        cadis=CategorieDisease.objects.all()
        for f in dis:
            dd= 0
            dd2=0
            for sur in SurveyingDisease.objects.filter(Disease_id=f.id):
                s = Surveying.objects.get(id=sur.Surveying_id)
                if sur.Surveying_id == s.id and s.date.month == self.month:
                    dd += sur.total
                if sur.Surveying_id == s.id and s.date.month == self.month-1:
                    dd2 += sur.total

            dis.filter(id=f.id).update(total=dd,month_last=dd2)
        for fcadis in cadis:
            tot = 0
            molast = 0
            for fdi in dis.filter(categorie_id=fcadis.id):
                tot+= fdi.total
                molast += fdi.month_last
            cadis.filter(id=fcadis.id).update(total=tot,month_last=molast)
        r="""
        
        <div class="row  border-top">
                                    <div class="col-3 border-left p-3">
                                        {}
                                    </div>
                                    <div class="col-1 border-left p-3">
                                        {}
                                    </div>
                                    <div class="col-2 border-left">
                                        <div class="row">
                                            <div class="col-6 p-3">
                                                {}
                                            </div> 
                                            <div class="col-6 border-left p-3">
                                               {}
                                            </div> 
                                        </div>
                                    </div>
                                    <div class="col-5 border-left p-1 text-left">
                                        -<br>-
                                    </div>
                                </div>
        
        """
        m = 1
        for f in cadis.order_by("-total"):
            if m <= 7:
                if f.total > f.month_last:
                    ma = f.total - f.month_last
                    mi = 0
                elif f.total < f.month_last:
                    ma = 0
                    mi = f.month_last - f.total
                else:
                    ma = 0
                    mi = 0
                re += r.format(f.name,f.total,ma,mi)
            m += 1
        return re
        
       

    def _(self):
        report_name = REPORTS[self.name-1][1]
        
        if self.month == None:
            month = "الأشهر الماضية"
        else:
            month = " شهر" +str(self.month)

        #if self.facility == None:
        facility = "جميع المحاور"
        #else:
        #    facility = "مرفق "+str(Facility.objects.get(id=self.facility).name)
          
    
        if self.name == 2:
            td = "<td>{}</td>"
        
            ths=""
            ths += "<th>اسم المرض</th>"
            trs = ""
            for f in Facility.objects.all():
                ths += "<th>{}</th>".format(f.name)
            ths += "<th>الإجمالي</th>"  
            for fd in Disease.objects.all():
                
                tds = ""
                tds += td.format(fd.name)
                fd_sum = 0
                for fa in Facility.objects.all():
                    fava = 0
                    
                    for fs in Surveying.objects.filter(facility__id=fa.id):
                        for fss in SurveyingDisease.objects.filter(Surveying__id=fs.id).filter(Disease__id=fd.id):
                            if fs.date.month == self.month:
                                fava += fss.total
                    fd_sum+=fava
                    tds += td.format(fava)
                tds += td.format(fd_sum)
                trs += "<tr>"+tds+"</tr>"
            rep = """
                    <table id="example" class="table table-sm table-bordered ">
                    <thead>
                    <tr>
                        """.format(date.now().date(),report_name,facility,month)+ths+"""
                    </tr>
                    </thead>
                    <tbody>
                    """ + trs + "</table>"
            return format_html(rep)
        elif self.name == 1:
            
            rep = """
            
                        <div class="text-primary text-center col-12 border-right">
                            <div class="row  border-top">
                                <div class="col-4">
                                    <div class="row border-bottom">
                                        <div class="col-12 border-left p-1">
                                            أولا: الحالات المرضية التي يجب التفريق بين الحالات المشتبهة والمؤكدة مخبرياّ
                                        </div>
                                    </div>
                                    <div class="row  border-bottom">  
                                        <div class="col-1 border-left p-2">
                                            م
                                        </div>
                                        <div class="col-6 border-left p-3">
                                            اسم المرض
                                        </div>
                                        <div class="col-5 border-left">
                                            <div class="row border-bottom">
                                                <div class="col-12 p-1">
                                                عدد الحالات
                                                </div>
                                            </div>
                                            <div class="row">
                                                <div class="col-7 p-0">
                                                    مؤكدة مخبرياً
                                                </div>
                                                <div class="col-5 border-left p-0">
                                                    مشتبهة
                                                </div>
                                            </div>
                                        </div>
                                    </div> """+self.مؤكدة_مخبريا()+"""
                                </div>

                                <div class="col-8">
                                    <div class="row border-bottom">
                                        <div class="col-12 p-1 border-left">
                                        <br>
                                            ثانياَ: حالات عامة
                                        </div>
                                    </div>
                                    <div class="row">  
                                        <div class="col-6">
                                            <div class="row  border-bottom">  
                                                <div class="col-1 border-left p-2">
                                                    م
                                                </div>
                                                <div class="col-8 border-left p-3">
                                                    اسم المرض
                                                </div>
                                                <div class="col-3 border-left p-1">
                                                    عدد الحالات
                                                </div>
                                            </div> """+self.حالات_عامة()+"""
                                        </div>
                                  
                                        <div class="col-6">
                                            <div class="row  border-bottom">  
                                                <div class="col-1 border-left p-2">
                                                    م
                                                </div>
                                                <div class="col-8 border-left p-3">
                                                    اسم المرض
                                                </div>
                                                <div class="col-3 border-left p-1">
                                                    عدد الحالات
                                                </div>
                                            </div> """+self.حالات_عامة_2()+"""
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                     """ + """
                     <br>
                     
                            <div class="text-primary text-center col-12 border-right">
                                <div class="row  border-top">
                                    <div class="col-2 border-left p-2 border-bottom">
                                        إجمالي الحالات المرضية في المديرية
                                    </div>
                                    <div class="col-2 border-left p-2 border-bottom">
                                        اجمالي الحالات التي عولجت في المرافق الطبية بالمديرية
                                    </div>
                                    <div class="col-4 border-right border-left">
                                        <div class="row border-bottom">
                                            <div class="col-12 p-3">
                                                الحالات المحولة خارج المديرية
                                            </div> 
                                        </div> 
                                        <div class="row border-bottom">
                                            <div class="col-2 p-1">
                                                العدد
                                            </div> 
                                            <div class="col-10 border-left p-1">
                                                أسباب التحويل
                                            </div> 
                                        </div>
                                    </div>
                                    <div class="col-4">
                                        <div class="row border-bottom">
                                            <div class="col-12 p-3">
                                                حالات الوفاة
                                            </div> 
                                        </div>
                                        <div class="row border-bottom">
                                            <div class="col-2 p-1">
                                                العدد
                                            </div> 
                                            <div class="col-10 border-left p-1">
                                                اسباب الوفاة
                                            </div> 
                                        </div>
                                    </div>
                                </div>
                                <div class="row  border-bottom">
                                    <div class="col-2 border-left p-4">
                                        """+self.اجمالي_الحالات()+"""
                                    </div>
                                    <div class="col-2 border-left p-4">
                                        """+self.اجمالي_الحالات_التي_عولجت()+"""
                                    </div>
                                    <div class="col-4 border-right border-left">
                                        <div class="row">
                                            <div class="col-2 p-4">
                                                5
                                            </div> 
                                            <div class="col-10 border-left p-1 text-left">
                                                -<br>-<br>-
                                            </div> 
                                        </div>
                                        
                                    </div>
                                    <div class="col-4">
                                        <div class="row">
                                            <div class="col-2 p-4">
                                                5
                                            </div> 
                                            <div class="col-10 border-left p-1 text-left">
                                                -<br>-<br>-
                                            </div> 
                                        </div>
                                        
                                    </div>
                                </div>
                            </div>


                    """+"""
                    <br>
                            <div class="text-primary text-center col-12 border-bottom border-right">
                                <div class="row  border-top">
                                    <div class="col-12 border-left p-3">
                                       أهم الأمراض المنتشرة
                                    </div>
                                </div>
                                <div class="row  border-top">
                                    <div class="col-3 border-left p-2">
                                        اسم المرض
                                    </div>
                                    <div class="col-1 border-left p-2">
                                        عدد الحالات
                                    </div>
                                    <div class="col-2 border-left">
                                        <div class="row">
                                            <div class="col-12 p-1">
                                                الفرق عن الشهر السابق
                                            </div> 
                                        </div> 
                                        <div class="row border-top">
                                            <div class="col-6">
                                                زيادة
                                            </div> 
                                            <div class="col-6 border-left">
                                                نقص
                                            </div> 
                                        </div>
                                    </div>
                                    <div class="col-5 border-left p-2">
                                    الأسباب
                                    </div>
                                </div>
                                """+self.الفرق()+"""
                            </div>   
                    """
            return format_html(rep)
    
    
    def a(self):
        return 5

    
class ReportDisease(Disease):
    
    class Meta:
        proxy=True
        '''Meta definition for MonthReport.'''
        verbose_name = 'التقرير اليومي'
        verbose_name_plural = 'التقرير اليومي'
    def الإجمالي(self):
        
        fava=0
        su = SurveyingDisease.objects.filter(Disease__id=self.id)
        if self.month == None:
            for f in su:
                fava += f.total
        else:
            for f in su:
                s = Surveying.objects.get(id=f.Surveying_id)
                if f.Surveying_id == s.id and s.date.month == self.month and s.facility_id == self.facility:
                    fava += f.total   
        return fava
    
    def total_day(self,de,month,day):
        va = 0
        su = SurveyingDisease.objects.filter(Disease__id=de)
        for f in su:
            s = Surveying.objects.get(id=f.Surveying_id)
            if f.Surveying_id == s.id and s.facility_id == self.facility and s.date.month == month and s.date.day == day:
                va += f.total
        if va == 0:
            return "_"
        else:

            return va
    def _1(self):
        return self.total_day(self.id,self.month,1)
    def _2(self):
        return self.total_day(self.id,self.month,2)
    def _3(self):
        return self.total_day(self.id,self.month,3)
    def _4(self):
        return self.total_day(self.id,self.month,4)
    def _5(self):
        return self.total_day(self.id,self.month,5)
    def _6(self):
        return self.total_day(self.id,self.month,6)
    def _7(self):
        return self.total_day(self.id,self.month,7)
    def _8(self):
        return self.total_day(self.id,self.month,8)
    def _9(self):
        return self.total_day(self.id,self.month,9)
    def _10(self):
        return self.total_day(self.id,self.month,10)
    def _11(self):
        return self.total_day(self.id,self.month,11)
    def _12(self):
        return self.total_day(self.id,self.month,12)
    def _13(self):
        return self.total_day(self.id,self.month,13)
    def _14(self):
        return self.total_day(self.id,self.month,14)
    def _15(self):
        return self.total_day(self.id,self.month,15)
    def _16(self):
        return self.total_day(self.id,self.month,16)
    def _17(self):
        return self.total_day(self.id,self.month,17)
    def _18(self):
        return self.total_day(self.id,self.month,18)
    def _19(self):
        return self.total_day(self.id,self.month,19)
    def _20(self):
        return self.total_day(self.id,self.month,20)
    def _21(self):
        return self.total_day(self.id,self.month,21)
    def _22(self):
        return self.total_day(self.id,self.month,22)
    def _23(self):
        return self.total_day(self.id,self.month,23)
    def _24(self):
        return self.total_day(self.id,self.month,24)
    def _25(self):
        return self.total_day(self.id,self.month,25)
    def _26(self):
        return self.total_day(self.id,self.month,26)
    def _27(self):
        return self.total_day(self.id,self.month,27)
    def _28(self):
        return self.total_day(self.id,self.month,28)
    def _29(self):
        return self.total_day(self.id,self.month,29)
    def _30(self):
        return self.total_day(self.id,self.month,30)
    



