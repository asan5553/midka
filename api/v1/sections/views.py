from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializer import SectionSerializer
from core.models import Section


class SectionViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = (AllowAny,)
