from rest_framework.viewsets import ModelViewSet
from adresses.models import End
from .serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    queryset = End.objects.all()
    serializer_class = AddressSerializer
