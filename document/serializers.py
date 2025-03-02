from rest_framework import serializers
from .models import DocType, DocApp


class DocTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocType
        fields = ('name', 'description')


class DocAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocApp
        fields = ('name', 'description')