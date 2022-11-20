from rest_framework import serializers

from ads.serializers import AdRetrieveSerializer
from selection.models import Selection


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ['id', 'name']


class SelectionRetrieveSerializer(serializers.ModelSerializer):
    items = AdRetrieveSerializer(many=True)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = '__all__'
