from django.contrib import admin
from django.contrib.auth.models import Group
from . models import Entry,AIS,FilesAdmin
# Register your models here.

class AISAdmin(admin.ModelAdmin):
    list_display = ('fleet_id','mmsi','timestamp')

admin.site.site_title ='ASEAN Hacks ADMIN'
admin.site.site_header ='Asean Hacks'
admin.site.index_title = "ADMIN DASHBOARD"

admin.site.unregister(Group)

admin.site.register(Entry)
admin.site.register(AIS,AISAdmin)
admin.site.register(FilesAdmin)