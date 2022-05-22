from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializer import ClassSerializer
from core.models import Class


class ClassViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (AllowAny,)

