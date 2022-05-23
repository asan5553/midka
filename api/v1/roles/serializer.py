from rest_framework import serializers

from core.models import Role1


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role1
        fields = "__all__"
