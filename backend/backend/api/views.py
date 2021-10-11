from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.views import APIView

from . import helpers


class Todo(APIView):
    def get(self, request, format=None):
        print(f"GET: {request}")
        if bearer_token := request.META.get('HTTP_AUTHORIZATION', None):
            if helpers.is_access_token_valid(bearer_token):
                return Response({"Token": bearer_token}, status=status.HTTP_200_OK)

            return Response({}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({}, status=status.HTTP_403_FORBIDDEN)


    def post(self, request, format=None):
        print(f"POST: {request}")
        return Response({}, status=200)


