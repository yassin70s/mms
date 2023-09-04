from django.contrib import admin
from .apps import mms_site
from .models import (
    Facility,
    CategorieDisease,Disease,
   
)




 

class DiseaseInline(admin.TabularInline):
    model = Disease
    extra=1
    fields = ["name"]
    verbose_name_plural = "الامراض"
class CategorieDiseaseAdmin(admin.ModelAdmin):
    fieldsets = (
        ("الفئة", {
            "fields": (
                "name",
            ),
        }),
    )
    
    inlines=[DiseaseInline]
admin.site.register(CategorieDisease,CategorieDiseaseAdmin)
class DiseaseAdmin(admin.ModelAdmin):
    list_display=["name"]
    list_filter=["categorie__name"]
    fields=["categorie","name"]
admin.site.register(Disease,DiseaseAdmin)


class FacilityInline(admin.TabularInline):
    model = Facility
    extra=1
@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass
