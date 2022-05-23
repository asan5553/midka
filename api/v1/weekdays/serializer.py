from rest_framework import serializers

from core.models import Weekday1


class WeekdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Weekday1
        fields = "__all__"
