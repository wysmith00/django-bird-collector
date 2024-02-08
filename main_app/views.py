from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Bird, Feeder, Perch
from .serializers import BirdSerializer, FeederSerializer, PerchSerializer, UserSerializer
# Define the home view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User




class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the bird-collector api home route!'}
    return Response(content)

class BirdList(generics.ListCreateAPIView):
  serializer_class = BirdSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
      # This ensures we only return cats belonging to the logged-in user
      user = self.request.user
      return Bird.objects.filter(user=user)

  def perform_create(self, serializer):
      # This associates the newly created cat with the logged-in user
      serializer.save(user=self.request.user)

class BirdDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = BirdSerializer
  lookup_field = 'id'

  def get_queryset(self):
    user = self.request.user
    return Bird.objects.filter(user=user)

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    perch_not_associated = perch.objects.exclude(id__in=instance.toys.all())
    perch_serializer = PerchSerializer(perch_not_associated, many=True)

    return Response({
        'bird': serializer.data,
        'perch_not_associated': perch_serializer.data
    })

  def perform_update(self, serializer):
    cat = self.get_object()
    if cat.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to edit this cat."})
    serializer.save()

  def perform_destroy(self, instance):
    if instance.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to delete this cat."})
    instance.delete()

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

class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })

# User Login
class LoginView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# User Verification
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })