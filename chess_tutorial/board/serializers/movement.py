from rest_framework import serializers

from board.models import Movement


class MovementSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = '__all__'