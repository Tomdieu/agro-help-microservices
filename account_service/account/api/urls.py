from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginViewSet, ValidateTokenView, ResetPasswordView, UpdatePasswordViewSet

router = DefaultRouter()
router.register('user', UserViewSet, basename='client')
router.register('auth', LoginViewSet, basename='login')
router.register('validate-token', ValidateTokenView,
                basename='validate-token')
router.register('reset-password', ResetPasswordView, basename='reset-password')

router.register('updated-password', UpdatePasswordViewSet,
                basename='updated-password')

urlpatterns = router.urls
