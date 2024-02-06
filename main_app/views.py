from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Bird, Feeder, Perch
from .serializers import BirdSerializer, FeederSerializer, PerchSerializer
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

  # add (override) the retrieve method below
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    # Get the list of toys not associated with this cat
    perch_not_associated = Perch.objects.exclude(id__in=instance.perch.all())
    perch_serializer = PerchSerializer(perch_not_associated, many=True)

    return Response({
        'bird': serializer.data,
        'perch_not_associated': perch_serializer.data
    })


class FeederListCreate(generics.ListCreateAPIView):
  serializer_class = FeederSerializer
  
  def get_queryset(self):
    bird_id = self.kwargs['bird_id']
    return Feeder.objects.filter(bird_id=bird_id)

  def perform_create(self, serializer):
    bird_id = self.kwargs['bird_id']
    bird = Bird.objects.get(id=bird_id)
    serializer.save(bird=bird)

class FeederDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = FeederSerializer
  lookup_field = 'id'

  def get_queryset(self):
    bird_id = self.kwargs['bird_id']
    return Feeder.objects.filter(bird_id=bird_id)

class PerchList(generics.ListCreateAPIView):
  queryset = Perch.objects.all()
  serializer_class = PerchSerializer

class PerchDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Perch.objects.all()
  serializer_class = PerchSerializer
  lookup_field = 'id'

class AddPerchToBird(APIView):
  def post(self, request, bird_id, perch_id):
    bird = Bird.objects.get(id=bird_id)
    perch = Perch.objects.get(id=perch_id)
    bird.perch.add(perch)
    return Response({'message': f'Perch {perch.name} added to Bird {bird.name}'})

