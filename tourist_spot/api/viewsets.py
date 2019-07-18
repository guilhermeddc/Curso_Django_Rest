from rest_framework.viewsets import ModelViewSet
from tourist_spot.api.serializers import TouristSpotSerializer
from tourist_spot.models import TouristSpot


class TouristSpotViewSet(ModelViewSet):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer
