from rest_framework.routers import DefaultRouter
from .views import SubscriptionTypeViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register(r'types', SubscriptionTypeViewSet, basename='subscriptiontype')
router.register(r'', SubscriptionViewSet)

urlpatterns = router.urls
