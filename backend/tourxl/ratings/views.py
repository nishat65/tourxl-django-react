from rest_framework.viewsets import ModelViewSet

from ratings.models import Ratings
from ratings.serializers import RatingsSerializer


class RatingsViewSet(ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer
