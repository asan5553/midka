from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializer import RoleSerializer
from core.models import Role1


class RoleViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Role1.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (AllowAny,)
