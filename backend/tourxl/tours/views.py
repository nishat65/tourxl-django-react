from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView

from tourxl.utils import predefinedJsonRes

from tours.models import Tours
from tours.serializers import ToursSerializer


class ReadTourModelViewSet(ReadOnlyModelViewSet):
    queryset = Tours.objects.all()
    serializer_class = ToursSerializer
