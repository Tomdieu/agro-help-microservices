from rest_framework.routers import DefaultRouter

from .views import SoilAreaViewSet, SoilViewSet

router = DefaultRouter()
router.register('soil_area', SoilAreaViewSet, basename='soil-area')
router.register('soil', SoilViewSet, basename='soil')

urlpatterns = router.urls