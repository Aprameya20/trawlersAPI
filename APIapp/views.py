from django.shortcuts import render
from django.http import FileResponse
from .models import Entry,AIS,FilesAdmin
from .serializers import EntrySerializer,mmsisSerializer,AISSerializer,FileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
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
    final=[]
    for i in serializer.data:
        if i.get("mmsi") not in final:
            final.append(i.get("mmsi"))
    return Response(final)

class FileViewSet(viewsets.ModelViewSet):
    queryset = FilesAdmin.objects.all()
    serializer_class = FileSerializer

def download(request, pk):
    obj = FilesAdmin.objects.get(id=pk)
    serializer = FileSerializer(obj)
    print(serializer.data)
    filename = obj.upload.path
    filename=filename[0:64]+"processed"+filename[69:-3]+"kml"
    response = FileResponse(open(filename, 'rb'))
    return response