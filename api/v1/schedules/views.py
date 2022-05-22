from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializer import ScheduleSerializer
from core.models import Schedule


class ScheduleViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (AllowAny,)
