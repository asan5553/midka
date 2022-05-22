from rest_framework import serializers
from core.models import Staff


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = '__all__'
