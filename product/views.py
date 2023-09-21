from rest_framework import viewsets
from models import Lesson
from serializers import LessonsListSerializer
from permissions import IsOwnerOrReadOnly


class LessonsViewSet(viewsets.ModelViewSet):
    # Вью для вывода списка уроков
    queryset = Lesson.objects.all()
    serializer_class = LessonsListSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['get'])
    def lessons(self, request, pk=None):
        product = self.get_object()
        lessons = product.lessons.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)
