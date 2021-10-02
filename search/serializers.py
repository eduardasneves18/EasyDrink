from django.db.models import fields
from django.db.models.base import Model
from .models import Search
from rest_framework import serializers

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Search
        fields = "__all__"