from rest_framework import serializers
from .models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    """Класс для сериализации моделек"""

    class Meta:
        model = Schedule
        # TODO: Вывести только названия группы, а не его айди
        fields = '__all__'
