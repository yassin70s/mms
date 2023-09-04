from typing import Dict, Optional
from django.contrib import admin
from django.http.request import HttpRequest
from django.template.response import TemplateResponse
from mysite.apps import mms_site
from django.shortcuts import render
import io
from django.http import FileResponse,HttpResponse

from mysite import models
from django.urls import path
from . import views
from datetime import datetime
# Register your models here.
date=datetime.now().date()
REPORTS = [
            (1,"تقرير إحصائي للحالات المرضية في جميع معسكرات التدريب التابعة للمنطقة"),
            (2,"تقرير إحصاء تفصيلي للمعسكرات"),
        ]
from .models import (
    
    Surveying, SurveyingDisease,
    Report,ReportDisease
)

class ReportFilter(admin.SimpleListFilter):
    title = ("اسم التقرير")
    parameter_name = "name"
    
    def lookups(self, request, model_admin):
        return REPORTS
    def queryset(self, request, queryset):
        if self.value():
            if queryset.count() == 0:
                queryset.create(id=1,name=self.value())
            elif queryset.count() == 1:
                queryset.update(name=self.value())
        else:
            queryset.delete()
        return queryset

class MonthFilter(admin.SimpleListFilter):
    title = ("إختار الشهر")
    parameter_name = "month"
    def lookups(self, request, model_admin):
        MONTHS=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12)]
        return MONTHS
    def queryset(self, request, queryset):
        if self.value():
            if queryset.count() != 0:
                queryset.update(month=self.value())
        return queryset
class FacilityFilter(admin.SimpleListFilter):
    title = ("جميع المرافق")
    parameter_name = "facility"
    facilitys = []
    for f in models.Facility.objects.all():
        facilitys += [(f.id,f.name)]
    def lookups(self, request, model_admin):
        return self.facilitys
    def queryset(self, request, queryset):
        if self.value():
            queryset.update(facility=self.value())
        return queryset


class SurveyingDiseaseInline(admin.TabularInline):
    model = SurveyingDisease
    
    extra=7


class Has:
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, obj):
        return False
    def has_delete_permission(self,obj=None):
        return False

@admin.register(Surveying)
class SurveyingAdmin(admin.ModelAdmin):
    list_display=["facility","date","count_surveying"]
    list_filter=["facility__name","date"]
    ordering=["date"]
    fieldsets = (
        ("البيانات الرئيسية", {
            "fields": (
                "facility","date",
            ),
        }),
    )
    inlines=[SurveyingDiseaseInline]
    @admin.display(description="إجمالي الحالات")
    def count_surveying(self,obj):
        co = 0
        for i in SurveyingDisease.objects.filter(Surveying=obj):
            co+=i.total
        return co





@admin.action(description="pdf")
def my_pdf(modeladmin, request, queryset):
    

    pass

@admin.action(description="prit")
def my_print(modeladmin, request, queryset):
    pass
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    #change_list_template="preventive/report.html"
    list_display=["_"]
    list_display_links=None
    actions=None
    list_filter=[ReportFilter,MonthFilter]
    def has_add_permission(self, request):
        return False
    def changelist_view(self, request, extra_context=None):
        extra_context = {
            "button_print":True,
        }
        return super().changelist_view(request, extra_context)

@admin.register(ReportDisease)
class ReportDiseaseAdmin(Has,admin.ModelAdmin):
    change_list_template="preventive/report.html"
    list_filter=["categorie__name",FacilityFilter,MonthFilter]
    list_display_links=None
    list_display=["name",
        "_1","_2","_3","_4","_5","_6","_7","_8","_9","_10",
        "_11","_12","_13","_14","_15","_16","_17","_18","_19","_20",
        "_21","_22","_23","_24","_25","_26","_27","_28","_29","_30",
        
        "الإجمالي"]
    list_per_page=15
    list_max_show_all = 300




