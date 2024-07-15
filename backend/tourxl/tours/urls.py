from django.urls import path
from rest_framework.routers import DefaultRouter

from tours.views import ReadTourModelViewSet

router = DefaultRouter()
router.register(r"tours", ReadTourModelViewSet, basename="tours")

urls = []

urlpatterns = urls + router.urls
