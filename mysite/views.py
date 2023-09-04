from django.shortcuts import render
from django.utils.datetime_safe import datetime
from .models import Disease,CategorieDisease,Facility
from preventive.models import Surveying,SurveyingDisease


def dd(CategorieDisease_id,Facility_id):
    da = 0
    for f in Disease.objects.filter(categorie_id=CategorieDisease_id):
        for ff in SurveyingDisease.objects.filter(Disease_id=f.id).filter(Surveying__facility_id=Facility_id):
            da += ff.total
    return da
def index(request):
    facility = []
    for f in Facility.objects.all():
        facility +=[f.name]
    categoriedisease=[]
    for f in CategorieDisease.objects.all():
        categoriedisease +=[f.name]

    dis = []
    for di in CategorieDisease.objects.all():
        d ={}
        d["label"] = di.name
        data = d["data"] = []
        for fa in Facility.objects.all():
            data += [dd(di.id,fa.id)]
        dis += [d]
    datacategoriedisease=[]
    
    for c in categoriedisease:
        data = 0
        for d in dis:
            if d["label"]== c :
                for f in d["data"]:
                    data += f
        datacategoriedisease += [data]



    context={
        "charts":{
            "labels":facility,
            "datasets":dis,
        },
        "donutchart":{
        "labels":categoriedisease,
        "datasets":datacategoriedisease,
        },
        "facility":Facility.objects.count(),
       

        "categorie_disease":CategorieDisease.objects.all(),
        "disease":Disease.objects.all(),
        
        
    }
    
    return (context)

