from rest_framework import generics, views
from .serializers import LocationSerializer, LocationTypeSerializer
from .models import Location, LocationType


class ListOrCreateLocationTypeView(generics.ListCreateAPIView):
    """ location type realated CRUD operations """
    queryset = LocationType.objects.all()
    serializer_class = LocationTypeSerializer
