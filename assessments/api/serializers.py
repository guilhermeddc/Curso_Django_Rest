from rest_framework.serializers import ModelSerializer
from assessments.models import Assessments


class AssessmentSerializer(ModelSerializer):
    class Meta:
        model = Assessments
        fields = ['id', 'user', 'comment', 'note', 'date']
