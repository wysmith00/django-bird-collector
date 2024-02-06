from rest_framework import serializers
from .models import Bird
from .models import Feeder

class FeederSerializer(serializers.ModelSerializer):
  class Meta:
    model = Feeder
    fields = '__all__'
    read_only_fields = ('bird',)


class BirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bird
        fields = '__all__'
