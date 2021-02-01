from django.shortcuts import render

from .models import Entry
from .serializers import EntrySerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
import datetime

@api_view(["POST"])
def EntryCreate(request):
    serializer = EntrySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def EntryDetails(request):
    list = []
    format_str='%Y-%m-%d'
    startdate= datetime.datetime.strptime(request.data.get("start"),format_str)
    enddate= datetime.datetime.strptime(request.data.get("end"),format_str)
    date=startdate
    stopcondition = enddate+datetime.timedelta(days=1)
    while (date!= stopcondition):

        Entries = Entry.objects.filter(date=date)
        serializer = EntrySerializer(Entries, many=True)
        if(serializer.data!=[]):
            list.append(serializer.data)
        date += datetime.timedelta(days=1)
    return Response(list)
