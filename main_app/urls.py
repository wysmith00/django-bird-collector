from django.urls import path
from .views import Home, BirdList, BirdDetail, FeederListCreate, FeederDetail, PerchList, PerchDetail, AddPerchToBird

urlpatterns = [
  path('', Home.as_view(), name='home'),
  # new routes below 
  path('bird/', BirdList.as_view(), name='bird-list'),
  path('birds/<int:id>/', BirdDetail.as_view(), name='bird-detail'),
  path('birds/<int:bird_id>/feeder/', FeederListCreate.as_view(), name='feeder-list-create'),
  path('birds/<int:bird_id>/feeder/<int:id>/', FeederDetail.as_view(), name='feeder-detail'),
  path('perch/', PerchList.as_view(), name='perch-list'),
  path('perch/<int:id>/', PerchDetail.as_view(), name='perch-detail'),
  path('birds/<int:bird_id>/add_perch/<int:perch_id>/', AddPerchToBird.as_view(), name='add-perch-to-bird'),
]
