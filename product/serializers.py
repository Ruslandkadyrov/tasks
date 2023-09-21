from rest_framework import serializers
from models import Lesson, ViewingLesson


class LessonsListSerializer(serializers.ModelSerializer):
    # Сериализатор для списка уроков
    class Meta:
        model = Lesson
        field = '__all__'


class ViewingLessonSerializer(serializers.ModelSerializer):
    # Сериализатор для статуса и времени просмотра
    class Meta:
        model = ViewingLesson
        field = '__all__'
