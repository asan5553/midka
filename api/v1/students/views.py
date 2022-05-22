from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializer import StudentSerializer
from core.models import Student


class StudentViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (AllowAny,)
