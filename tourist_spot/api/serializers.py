from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from tourist_spot.models import TouristSpot
from attractions.api.serializers import AttractionsSerializer
from adresses.api.serializers import AddressSerializer
from comments.api.serializers import CommentsSerializer
from assessments.api.serializers import AssessmentSerializer


class TouristSpotSerializer(ModelSerializer):
    attractions = AttractionsSerializer(many=True)
    comments = CommentsSerializer(many=True)
    assessments = AssessmentSerializer(many=True)
    # end = AddressSerializer()
    description_complete = SerializerMethodField()

    class Meta:
        model = TouristSpot
        fields = (
            'id', 'name', 'descriptions', 'approved', 'photo',
            'attractions', 'comments', 'assessments', 'description_complete', 'description_complete_two',
        )

    def get_description_complete(self, obj):
        return '%s - %s' % (obj.name, obj.descriptions)
