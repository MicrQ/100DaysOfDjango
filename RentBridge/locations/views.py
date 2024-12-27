from rest_framework import generics, views
from .serializers import LocationSerializer, LocationTypeSerializer
from .models import Location, LocationType
from rent_bridge.permissions import IsAdminOrReadOnly


class ListOrCreateLocationTypeView(generics.ListCreateAPIView):
    """ location type realated CRUD operations """
    queryset = LocationType.objects.all()
    serializer_class = LocationTypeSerializer
    permission_classes = [IsAdminOrReadOnly]


class RetrieveUpdateDestroyLocationTypeView(
     generics.RetrieveUpdateDestroyAPIView):
    """ location type realated CRUD operations """
    queryset = LocationType.objects.all()
    serializer_class = LocationTypeSerializer
    permission_classes = [IsAdminOrReadOnly]
