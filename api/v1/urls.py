from rest_framework.routers import DefaultRouter
from .classes.views import ClassViewSet
from .lessons.views import LessonViewSet
from .roles.views import RoleViewSet
from .schedules.views import ScheduleViewSet
from .sections.views import SectionViewSet
from .staffs.views import StaffViewSet
from .students.views import StudentViewSet
from .weekdays.views import WeekdayViewSet

router = DefaultRouter()
router.register("classes", ClassViewSet, basename="classes")
router.register("lessons", LessonViewSet, basename="lessons")
router.register("roles", RoleViewSet, basename="roles")
router.register("schedules", ScheduleViewSet, basename="schedules")
router.register("sections", SectionViewSet, basename="sections")
router.register("staffs", StaffViewSet, basename="staffs")
router.register("students", StudentViewSet, basename="students")
router.register("weekdays", WeekdayViewSet, basename="weekdays")

urlpatterns = [
]

urlpatterns += router.urls
