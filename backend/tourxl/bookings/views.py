from django.db.models import Count, Aggregate

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from bookings.models import Bookings
from tours.models import Tours
from bookings.serializers import BookingsSerializer, ToursBookingSerializer

from tourxl.utils import predefinedJsonRes


class BookingsViewSet(ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer


class BookingsView(APIView):
    def get(self, request):
        bookings = (
            Bookings.objects.select_related("customer_id", "guide_id", "tour_id")
            # .filter(tour_id__name__startswith="City Heritage Walk")
            .all()
        )
        tb = Bookings.objects.aggregate(total_bookings=Count("id"))
        serializer = BookingsSerializer(bookings, many=True).data
        data = {
            "bookings": serializer,
            "total_bookings": tb["total_bookings"],
        }
        return Response(
            data=predefinedJsonRes(message="Bookings fetched", data=data),
            status=HTTP_200_OK,
        )


class ToursView(APIView):
    def get(self, request):
        tours = Tours.objects.prefetch_related("tours").all()
        serializer = ToursBookingSerializer(tours, many=True).data
        return Response(
            data=predefinedJsonRes(message="Tours fetched", data=serializer),
            status=HTTP_200_OK,
        )
