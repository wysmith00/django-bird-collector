from rest_framework import serializers
from .models import Bird
from .models import Feeder
from .models import Perch

class FeederSerializer(serializers.ModelSerializer):
  class Meta:
    model = Feeder
    fields = '__all__'
    read_only_fields = ('bird',)


class BirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bird
        fields = '__all__'

class PerchSerializer(serializers.ModelSerializer):
   class Meta:
      model = Perch
      fields = '__all__'
