from django.shortcuts import render
from .models import OperaSms
from mysite.models import Facility,Disease
from preventive.models import Surveying,SurveyingDisease
from django.utils.timezone import datetime
# Create your views here.

def lsc(request):
    date_naw = datetime.now().date()
    for fa in Facility.objects.all():
        surveying_facility = Surveying.objects.filter(facility=fa)
        if not surveying_facility.filter(date=date_naw).exists():
            content_message = f""
    messages = [{'phone':'111','id':1,'content':'السdكري:2.'}]
    con = "ff"
    for message in messages:
        if Facility.objects.filter(name=message['phone']).exists() and not OperaSms.objects.filter(id_message=message['id']).exists():
            facility = Facility.objects.get(name=message['phone'])
            content_list = message['content'].split(".")
            error_count = 0
            error_list = []
            data_list=[]
            for i in range(len(content_list)):
                    data={}
                    error={}
                    content_raw = content_list[i].split(":")
                    if len(content_raw) >= 2:
                        key = content_raw[0]
                        val = content_raw[1]
                        if Disease.objects.filter(name=key).exists():
                            data['disease'] = Disease.objects.get(name=key)
                            data["total"] = int(val)
                            data_list+=[data]
                        else:
                            error['key'] = key
                            error['val'] = val
                            error['error'] = "غير موجود"
                            error_list +=[error]





            if len(error_list)==0:
                Surveying.objects.update_or_create(
                    facility=facility,
                    date=date_naw,
                )
                for d in data_list:
                    surveying=Surveying.objects.get(
                        facility=facility,
                        date=date_naw,
                    )
                    SurveyingDisease.objects.create(
                        Surveying=surveying,
                        Disease=d['disease'],
                        total=d['total']
                    )
                con = "تم الحفظ"
            else:
                con=error_list
    return render(request,"lsc.html",{'con':con})
