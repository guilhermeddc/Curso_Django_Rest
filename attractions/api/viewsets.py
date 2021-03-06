# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from attractions.models import Attractions
from .serializers import AttractionsSerializer


class AttractionViewSet(ModelViewSet):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer
    # filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'minimumAge')
