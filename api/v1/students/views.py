from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.models import Student

from .serializer import StudentSerializer


class StudentViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (AllowAny,)
