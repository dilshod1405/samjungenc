from rest_framework import serializers
from chiller.models import Chiller, ChillerImage


class ChillerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chiller
        fields = '__all__'

class ChillerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChillerImage
        fields = '__all__'