from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView 
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

# Create your views here.
class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all() 
    serializer_class = MenuSerializer 
    permission_classes = [IsAuthenticated,]

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all() 
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated,]

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all() 
    serializer_class = BookingSerializer 
    permission_classes = [IsAuthenticated,]