from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializer import LessonSerializer
from core.models import Lesson


class LessonViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (AllowAny,)
