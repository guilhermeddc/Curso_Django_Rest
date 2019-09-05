from rest_framework.serializers import ModelSerializer
from adresses.models import Adresses


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Adresses
        fields = ['line1', 'line2', 'city', 'state', 'country',
                  'latitude', 'longitude']
