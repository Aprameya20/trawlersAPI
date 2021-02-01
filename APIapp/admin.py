from django.contrib import admin
from django.contrib.auth.models import Group
from . models import Entry
# Register your models here.


admin.site.site_title ='ASEAN Hacks ADMIN'
admin.site.site_header ='Asean Hacks'
admin.site.index_title = "ADMIN DASHBOARD"

admin.site.unregister(Group)

admin.site.register(Entry)