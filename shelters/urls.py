from rest_framework.routers import DefaultRouter
from .views import ShelterViewSet, PendingCheckinViewSet

router = DefaultRouter()
router.register('shelters', ShelterViewSet)
router.register('checkins', PendingCheckinViewSet)

urlpatterns = router.urls