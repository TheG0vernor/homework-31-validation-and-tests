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
        return request.user

    def _can_create(self):
        request = self.context.get('request', None)
        if request.user.role in ('moderator', 'admin'):
            return True

    def create(self, validated_data):
        if "owner" not in validated_data:
            validated_data['owner'] = self._get_owner()
        elif "owner" in validated_data and not self._can_create():
            raise PermissionError("Not enough permissions")
        return super().create(validated_data)

    class Meta:
        model = Selection
        fields = ['id', 'name', 'items', 'owner']