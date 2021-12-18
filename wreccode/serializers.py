from django.db import models
from django.db.models.base import ModelState
from rest_framework import serializers
from .models import Responses


class ResponseSerializer(serializers.ModelSerializer):
    # args = serializers.JSONField()
    # data = serializers.CharField(max_length=12, default={})
    # file = serializers.CharField(max_length=12, default={})
    # form = serializers.CharField(max_length=12, default={})
    class Meta:
        model = Responses
        fields = ['data', 'args', 'file', 'form']