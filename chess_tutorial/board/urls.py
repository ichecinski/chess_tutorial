from django.urls import path, include
from rest_framework import routers

from .views import chessman as chessman_views
from .views import board_session as board_views

routers = routers.DefaultRouter()

routers.register('chess-types', chessman_views.ChessTypeView, basename='chess-types')
routers.register('chess-colors', chessman_views.ChessColorsView, basename='chess-colors')
routers.register('chessman', chessman_views.ChessmanView, basename='chessman')
routers.register('chessman/move', chessman_views.ChessmanMoveView, basename='chessman-move')
routers.register('chessman/movements', chessman_views.ChessmanMovementView, basename='chessman-movements')
routers.register('board-session/chessman/add', board_views.BoardSessionChessmanAddView, basename='board-session-add-chessman')
routers.register('board-session', board_views.BoardSessionView, basename='board-session')

urlpatterns = [
    path('', include(routers.urls))
]