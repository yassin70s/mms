from django.apps import AppConfig

class MysiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mysite'

from django.contrib import admin


class MmsAdminArea(admin.AdminSite):
    pass
mms_site = MmsAdminArea(name='MmsAdmin')
mms_site.site_header = 'الخدمات الطبية العسكرية'
mms_site.site_title = 'الخدمات الطبية'
mms_site.index_title='الرئيسية'
mms_site.index_template="mysite/index.html"


