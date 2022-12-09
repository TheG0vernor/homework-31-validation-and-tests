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


class SelectionUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    def _get_owner(self):
        request = self.context.get('request', None)
        if request.user.role not in ('moderator', 'admin'):
            return request.user

    def create(self, validated_data):
        if self._get_owner():
            validated_data['owner'] = self._get_owner()
        return super().create(validated_data)

    class Meta:
        model = Selection
        fields = ['id', 'name', 'items', 'owner']