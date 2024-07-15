from django.db.models import Count, Sum
from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from tourxl.utils import predefinedJsonRes
from tourxl.constants import users
from .serializers import GuidesSerializer
from .models import Guides


# Create your views here.
class GuidesView(ModelViewSet):
    serializer_class = GuidesSerializer
    queryset = Guides.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ("email", "phone", "first_name", "last_name")


class GuidesGetViews(APIView):
    def get(self, request):
        email = request.query_params.get("email", None)
        qs = Guides.objects.filter(email__startswith=email).first()
        # average_tours = Guides.objects.values("total_tours_done").annotate(
        #     count=Count("total_tours_done")
        # )
        # average_tours = Guides.objects.annotate(total_tours=Sum("total_tours_done"))
        # print(average_tours)
        serializer = GuidesSerializer(qs).data
        return Response(
            data=predefinedJsonRes(message=users["USERS_FETCHED"], data=serializer),
            status=HTTP_200_OK,
        )
