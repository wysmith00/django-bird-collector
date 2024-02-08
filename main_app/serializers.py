from rest_framework import serializers
from .models import Bird
from .models import Feeder
from .models import Perch
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
      user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']  # Ensures the password is hashed correctly
      )
      
      return user

# class BirdSerializer(serializers.ModelSerializer):
#   fed_for_today = serializers.SerializerMethodField()
#   perch = PerchSerializer(many=True, read_only=True)
#   # add user field to Cat serializer
#   user = serializers.PrimaryKeyRelatedField(read_only=True)







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
  
  class BirdSerializer(serializers.ModelSerializer):
    fed_for_today = serializers.SerializerMethodField()
    perch = PerchSerializer(many=True, read_only=True)
  # add user field to Cat serializer
    user = serializers.PrimaryKeyRelatedField(read_only=True)



