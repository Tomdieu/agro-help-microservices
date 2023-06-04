from rest_framework.routers import DefaultRouter


from . import views

router = DefaultRouter()

router.register("forum", views.ForumViewSet, basename="forum")
router.register("forum-comment", views.ForumCommentViewSet, basename="forum-post")

urlpatterns = []

urlpatterns += router.urls
