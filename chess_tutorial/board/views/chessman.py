from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from board.logic.enums import ChessType
from board.models import Chessman
from board.serializers.chessman import ChessmanMoveSerializer, ChessmanSerializer
from board.serializers.movement import MovementSerialzier


class ChessTypeView(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return ChessType._member_names_

    def list(self, request, *args, **kwargs):
        return Response(self.get_queryset())


class ChessColorsView(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Chessman.Color._member_names_

    def list(self, request, *args, **kwargs):
        return Response(self.get_queryset())


class ChessmanView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Chessman.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ChessmanSerializer


class ChessmanMoveView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Chessman.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ChessmanMoveSerializer


class ChessmanMovementView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Chessman.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = MovementSerialzier

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object().movements.all()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)