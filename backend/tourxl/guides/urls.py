from rest_framework.routers import DefaultRouter
from guides.views import GuidesView
from guides.views import GuidesGetViews

from django.urls import path

router = DefaultRouter()

router.register(r"guides", GuidesView, basename="guides")

urls = [
    path("guide/views", GuidesGetViews.as_view(), name="get guides"),
]

urlpatterns = urls + router.urls
