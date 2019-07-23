from rest_framework.serializers import ModelSerializer
from attractions.models import Attractions


class AttractionsSerializer(ModelSerializer):

    class Meta:
        model = Attractions
        fields = ('id', 'name', 'description', 'workingHours', 'minimumAge')
