from django.shortcuts import render

from .models import Entry
from .serializers import EntrySerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(["POST"])
def EntryCreate(request):
    serializer = EntrySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def EntryDetails(request,pk):
    Entries = Entry.objects.filter(date=pk)
    serializer = EntrySerializer(Entries,many=True)
    return Response(serializer.data)
