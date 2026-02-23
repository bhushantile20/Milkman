from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MilkmanProfileViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')
router.register(r'profiles', MilkmanProfileViewSet, basename='milkmanprofile')

urlpatterns = router.urls
