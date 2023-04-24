from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import PostViewSet, UserViewSet

router = SimpleRouter()

router.register("users", PostViewSet, basename="users"),
router.register("", UserViewSet, basename="posts"),

urlpatterns = router.urls
