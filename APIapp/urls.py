from django.urls import path
from . import views

urlpatterns=[
    path('entry-create/', views.EntryCreate, name="entry-create"),
    path('entry-details/', views.EntryDetails, name="entry-details"),
    path('ais-details/<str:pk>', views.AISDetails, name="ais-details"),
    path('fleet-details/<int:pk>', views.FleetDetails, name="fleet-details"),
]