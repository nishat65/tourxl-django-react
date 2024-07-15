from rest_framework.serializers import ModelSerializer
from guides.models import Guides


class GuidesSerializer(ModelSerializer):
    class Meta:
        model = Guides
        fields = "__all__"
