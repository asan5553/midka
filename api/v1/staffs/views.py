from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.models import Staff

from .serializer import StaffSerializer


class StaffViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (AllowAny,)
