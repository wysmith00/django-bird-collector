from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Bird, Feeder
from .serializers import BirdSerializer, FeederSerializer
# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the bird-collector api home route!'}
    return Response(content)

class BirdList(generics.ListCreateAPIView):
  queryset = Bird.objects.all()
  serializer_class = BirdSerializer

class BirdDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Bird.objects.all()
  serializer_class = BirdSerializer
  lookup_field = 'id'

class FeederListCreate(generics.ListCreateAPIView):
  serializer_class = FeederSerializer

  def get_queryset(self):
    bird_id = self.kwargs['bird_id']
    return Feeder.objects.filter(bird_id=bird_id)

  def perform_create(self, serializer):
    bird_id = self.kwargs['bird_id']
    cat = Bird.objects.get(id=bird_id)
    serializer.save(bird=bird)

class FeederDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = FeederSerializer
  lookup_field = 'id'

  def get_queryset(self):
    bird_id = self.kwargs['bird_id']
    return Feeder.objects.filter(bird_id=bird_id)

