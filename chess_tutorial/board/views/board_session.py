from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from board.models import BoardSession
from board.serializers.board_session import BoardSessionSerializer, BoardSessionAddChessmanSerializer


class BoardSessionView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = BoardSession.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = BoardSessionSerializer


class BoardSessionChessmanAddView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = BoardSession.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = BoardSessionAddChessmanSerializer