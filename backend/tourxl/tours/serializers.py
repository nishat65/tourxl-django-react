from rest_framework.serializers import (
    ModelSerializer,
)
from tours.models import Tours


class ToursSerializer(ModelSerializer):
    class Meta:
        model = Tours
        fields = "__all__"
