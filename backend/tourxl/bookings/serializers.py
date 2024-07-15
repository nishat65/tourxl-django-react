from rest_framework.serializers import ModelSerializer, StringRelatedField, IntegerField

from customers.serializers import CustomersSerializer
from guides.serializers import GuidesSerializer

from tours.serializers import ToursSerializer
from tours.models import Tours

from bookings.models import Bookings


class BookingsSerializer(ModelSerializer):
    customer_id = StringRelatedField()
    guide_id = StringRelatedField()
    tour_id = ToursSerializer()

    class Meta:
        model = Bookings
        fields = "__all__"


class ToursBookingSerializer(ModelSerializer):
    tours = BookingsSerializer(many=True)

    class Meta:
        model = Tours
        fields = "__all__"
