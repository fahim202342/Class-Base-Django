from rest_framework import serializers
from rest_framework.response import Response
from api_app.serializers import *
from api_app.models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'