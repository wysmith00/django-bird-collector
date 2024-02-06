from rest_framework import serializers
from .models import Bird
from .models import Feeder
from .models import Perch

class FeederSerializer(serializers.ModelSerializer):
  class Meta:
    model = Feeder
    fields = '__all__'
    read_only_fields = ('bird',)

class PerchSerializer(serializers.ModelSerializer):
   class Meta:
      model = Perch
      fields = '__all__'



class BirdSerializer(serializers.ModelSerializer):
  feeder_for_today = serializers.SerializerMethodField()
  perch = PerchSerializer(many=True, read_only=True) #add this line

  class Meta:
    model = Bird
    fields = '__all__'

  def get_feeder_for_today(self, obj):
    return obj.feeder_for_today()


