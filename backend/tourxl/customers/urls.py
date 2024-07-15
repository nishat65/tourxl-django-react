from rest_framework.routers import DefaultRouter

from customers.views import CustomersViewSet

router = DefaultRouter()

router.register(r"customers", CustomersViewSet, basename="customers")

urlpatterns = router.urls
