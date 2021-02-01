from django.urls import path
from . import views

urlpatterns=[
    path('entry-create/', views.EntryCreate, name="entry-create"),
    path('entry-details/<str:pk>/', views.EntryDetails, name="entry-details"),
]