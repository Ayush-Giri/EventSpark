from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from custom_permissions import IsOrganiser, IsEventOwner
from rest_framework.permissions import IsAuthenticated
from event.serializers import EventSerializer
from event.models import Event
from pagination import BasicPagination

# Create your views here.

class EvenViewSet(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsEventOwner, IsOrganiser, IsAuthenticated]
    queryset = Event.objects.all()
    pagination_class = BasicPagination


    def get_permissions(self):
        if self.action in ["list"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsOrganiser, IsEventOwner]
        return [permission() for permission in permission_classes]