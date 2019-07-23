from rest_framework.viewsets import ModelViewSet
from adresses.models import Adresses
from .serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    queryset = Adresses.objects.all()
    serializer_class = AddressSerializer
