from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from api.serializers import TodoSerializer
from api.models import Todo

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class TodoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user__email=self.request.user.email).all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(todo)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        if request.user.email == todo.user.email:
            return super().destroy(request, *args, **kwargs)
        return Response({}, status=status.HTTP_404_NOT_FOUND)






