from rest_framework import serializers
from api.models import Todo
from django.contrib.auth import get_user_model




class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'

