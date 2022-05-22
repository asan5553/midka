from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializer import WeekdaySerializer
from core.models import Weekday1


class WeekdayViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Weekday1.objects.all()
    serializer_class = WeekdaySerializer
    permission_classes = (AllowAny,)
