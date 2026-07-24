from rest_framework.routers import DefaultRouter
from event.views import EvenViewSet
from django.urls import path, include

router = DefaultRouter()
router.regsiter(r'events', EvenViewSet)

urlpatterns = [
    path('', include(router.urls))
]