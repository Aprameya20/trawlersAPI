from django.urls import path
from . import views
from.views import FileViewSet

from django.conf.urls import include,url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'files',FileViewSet)

urlpatterns=[
    path('entry-create/', views.EntryCreate, name="entry-create"),
    path('entry-details/', views.EntryDetails, name="entry-details"),
    path('ais-details/<str:pk>', views.AISDetails, name="ais-details"),
    path('fleet-details/<int:pk>', views.FleetDetails, name="fleet-details"),
    path('download/<int:pk>',views.download,name="download"),
    #path('upload/', views.FileViewSet.as_view(), name="upload"),
    url(r'^',include(router.urls)),
]