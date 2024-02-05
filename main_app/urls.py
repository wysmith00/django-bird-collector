from django.urls import path
from .views import Home, BirdList, BirdDetail

urlpatterns = [
  path('', Home.as_view(), name='home'),
  # new routes below 
  path('bird/', BirdList.as_view(), name='bird-list'),
  path('birds/<int:id>/', BirdDetail.as_view(), name='bird-detail'),
]
