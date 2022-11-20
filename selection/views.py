from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from selection.models import Selection
from selection.permission import SelectionPermission
from selection.serializers import SelectionListSerializer, SelectionCUDSerializer, SelectionRetrieveSerializer


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()

    default_serializer = SelectionCUDSerializer
    default_permission = [AllowAny()]

    serializer_classes = {
        'list': SelectionListSerializer,
        'retrieve': SelectionRetrieveSerializer,
    }

    permissions = {
        'create': [IsAuthenticated()],
        'update': [IsAuthenticated(), SelectionPermission()],
        'destroy': [IsAuthenticated(), SelectionPermission()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)
