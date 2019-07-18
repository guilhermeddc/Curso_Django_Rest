from rest_framework.serializers import ModelSerializer
from tourist_spot.models import TouristSpot


class TouristSpotSerializer(ModelSerializer):
    class Meta:
        model = TouristSpot
        fields = ('id', 'name', 'descriptions')
