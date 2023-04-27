import enum
from board.logic import logic


class ChessType(enum.Enum):
    PAWN = 'PAWN', logic.PawnLogic
    ROOK = 'ROOK', logic.RookLogic
    KNIGHT = 'KNIGHT', logic.KnightLogic
    BISHOP = 'BISHOP', logic.BishopLogic
    KING = 'KING', logic.KnightLogic
    QUEEN = 'QUEEN', logic.KnightLogic

    @classmethod
    def choices(cls):
        return [e.value for e in cls]

    @classmethod
    def logic(cls, type_: str):
        return ChessType[type_].value[1]