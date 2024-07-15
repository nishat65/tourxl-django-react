from rest_framework.serializers import ModelSerializer
from ratings.models import Ratings


class RatingsSerializer(ModelSerializer):
    class Meta:
        model = Ratings
        fields = "__all__"
