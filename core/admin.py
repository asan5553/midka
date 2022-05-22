from django.contrib import admin

from .models import (
    Class, Lesson, Role1, Schedule, Staff, Section, Weekday1
)


admin.site.register(Class)
admin.site.register(Lesson)
admin.site.register(Role1)
admin.site.register(Schedule)
admin.site.register(Staff)
admin.site.register(Section)
admin.site.register(Weekday1)
