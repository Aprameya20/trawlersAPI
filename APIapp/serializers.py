from rest_framework import serializers
from . models import Entry,AIS,FilesAdmin

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

class mmsisSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIS
        fields = ('mmsi',)

class AISSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIS
        fields = ('mmsi',
                  'timestamp',
                  'lat',
                  'lon',
                )

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilesAdmin
        fields = ('upload','title')