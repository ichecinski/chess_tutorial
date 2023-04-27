from abc import ABC, abstractmethod


class ChessmanLogic(ABC):
    def __init__(self, chessman: 'Chesman'):
        self.__chessman = chessman

    @property
    @abstractmethod
    def movement_pattern(self) -> list[tuple[int, int]]:
        pass

    @property
    @abstractmethod
    def limit_to_one_move(self) -> bool:
        pass

    @property
    def chessman(self):
        self.__chessman.refresh_from_db()
        return self.__chessman

    @property
    def allowed_movements(self) -> list[tuple[int, int]]:
        if self.limit_to_one_move:
            return self._limited_movement()
        return self._unlimited_movement()

    def is_movement_overlapping_with_other_chessman(self, expected_x: int, expected_y: int) -> bool:
        return self.chessman.board_session.chessmans.filter(pos_x=expected_x, pos_y=expected_y).exists()

    def is_movement_allowed(self, expected_x: int, expected_y: int):
        if self.is_movement_overlapping_with_other_chessman(expected_x=expected_x, expected_y=expected_y):
            return False
        return (expected_x, expected_y) in self.allowed_movements

    def _limited_movement(self) -> list[tuple[int, int]]:
        generated_movements = [(self.chessman.pos_x + pos[0], self.chessman.pos_y + pos[1]) for pos in self.movement_pattern]
        return self._clear_out_of_bounnd_movements(movements=generated_movements)

    def _unlimited_movement(self) -> list[tuple[int, int]]:
        generated_movements = [(self.chessman.pos_x + pos[0] * i, self.chessman.pos_y + pos[0] * i) for pos in self.movement_pattern for i in
                               range(1, 8)]
        return self._clear_out_of_bounnd_movements(movements=generated_movements)

    def _clear_out_of_bounnd_movements(self, movements: list[tuple[int, int]]) -> list[tuple[int, int]]:
        return [(pos[0], pos[1]) for pos in movements if 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7]


class PawnLogic(ChessmanLogic):
    @property
    def movement_pattern(self) -> list[tuple[int, int]]:
        return [(0, 1), (0, -1), (1, 0), (-1, 0)]

    @property
    def limit_to_one_move(self) -> bool:
        return True


class RookLogic(ChessmanLogic):
    @property
    def movement_pattern(self) -> list[tuple[int, int]]:
        return [(0, 1), (0, -1), (1, 0), (-1, 0)]

    @property
    def limit_to_one_move(self) -> bool:
        return False


class KnightLogic(ChessmanLogic):
    @property
    def movement_pattern(self) -> list[tuple[int, int]]:
        return [
            (1, 2), (2, 1), (1, -2), (2, -1),
            (-1, 2), (-2, 1), (-1, -2), (-2, -1),
        ]

    @property
    def limit_to_one_move(self) -> bool:
        return True


class BishopLogic(ChessmanLogic):
    @property
    def movement_pattern(self) -> list[tuple[int, int]]:
        return [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    @property
    def limit_to_one_move(self) -> bool:
        return False


class KingLogic(ChessmanLogic):
    @property
    def movement_pattern(self) -> list[tuple[int, int]]:
        return [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    @property
    def limit_to_one_move(self) -> bool:
        return True


class QueenLogic(ChessmanLogic):
    @property
    def movement_pattern(self) -> list[tuple[int, int]]:
        return [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    @property
    def limit_to_one_move(self) -> bool:
        return True


class QueenLogic(ChessmanLogic):
    @property
    def movement_pattern(self) -> list[tuple[int, int]]:
        return [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    @property
    def limit_to_one_move(self) -> bool:
        return False