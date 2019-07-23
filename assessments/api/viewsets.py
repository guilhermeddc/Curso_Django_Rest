from rest_framework.viewsets import ModelViewSet
from .serializers import AssessmentSerializer
from assessments.models import Assessments


class AssessmentViewSet(ModelViewSet):
    queryset = Assessments.objects.all()
    serializer_class = AssessmentSerializer
