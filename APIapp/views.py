from django.shortcuts import render

from .models import Entry,AIS
from .serializers import EntrySerializer,mmsisSerializer,AISSerializer

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


@api_view(["GET"])
def AISDetails(request,pk):
    aises = AIS.objects.filter(fleet_id=pk)
    serializer = AISSerializer(aises, many=True)
    final=[]
    for i in serializer.data:
        latest=i
        for j in serializer.data:
            if (j.get("mmsi")==latest.get("mmsi")):
                if (j.get("timestamp")>latest.get("timestamp")):
                    latest=j
        if latest not in final:
            final.append(latest)
    return Response(final)


@api_view(["GET"])
def FleetDetails(request,pk):
    mmsis = AIS.objects.filter(fleet_id=pk)
    serializer = mmsisSerializer(mmsis, many=True)
    return Response(serializer.data)