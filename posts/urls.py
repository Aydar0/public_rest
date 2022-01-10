from django.urls import path
from rest_framework import routers
from .views import PostViewset, UserViewset

router = routers.SimpleRouter()

router.register('users', UserViewset, basename='users')
router.register('', PostViewset, basename='posts')

urlpatterns = router.urls