from rest_framework.routers import DefaultRouter
from django.urls import path
from bookings.views import BookingsViewSet, BookingsView, ToursView

router = DefaultRouter()

router.register(r"bookings", BookingsViewSet, basename="bookings")

urls = [
    path("bookings/views", BookingsView.as_view(), name="bookings/views"),
    path("tours/views", ToursView.as_view(), name="tours/views"),
]

urlpatterns = urls + router.urls
