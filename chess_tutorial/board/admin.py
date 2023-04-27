from django import forms
from django.contrib import admin

from board import models
from board.logic.enums import ChessType


class AdminChessmanForm(forms.ModelForm):
    CHESSMAN_TYPES = [
        (ChessType.PAWN.value[0], ChessType.PAWN.value[0]),
        (ChessType.ROOK.value[0], ChessType.ROOK.value[0]),
        (ChessType.KNIGHT.value[0], ChessType.KNIGHT.value[0]),
        (ChessType.BISHOP.value[0], ChessType.BISHOP.value[0]),
        (ChessType.KING.value[0], ChessType.KING.value[0]),
        (ChessType.QUEEN.value[0], ChessType.QUEEN.value[0]),
    ]

    def __init__(self, *args, **kwargs):
        super(AdminChessmanForm, self).__init__(*args, **kwargs)
        self.fields['type'] = forms.ChoiceField(required=True, choices=self.CHESSMAN_TYPES)


@admin.register(models.Chessman)
class AdminChessmanModel(admin.ModelAdmin):
    form = AdminChessmanForm

    readonly_fields = ('movements',)


@admin.register(models.BoardSession)
class AdminBoardSessionModel(admin.ModelAdmin):
    pass