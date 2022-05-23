from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.models import Class

from .serializer import ClassSerializer


class ClassViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (AllowAny,)
