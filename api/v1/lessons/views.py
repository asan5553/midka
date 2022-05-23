from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.models import Lesson

from .serializer import LessonSerializer


class LessonViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (AllowAny,)
