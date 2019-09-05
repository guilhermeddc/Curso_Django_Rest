from rest_framework.serializers import ModelSerializer
from adresses.models import End


class AddressSerializer(ModelSerializer):
    class Meta:
        model = End
        fields = ['line1', 'line2', 'city', 'state', 'country',
                  'latitude', 'longitude']
