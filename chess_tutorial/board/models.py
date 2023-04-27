import uuid

from django.db import models

from board.logic.enums import ChessType


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

    @property
    def id_to_str(self):
        return str(self.id)

    def __str__(self):
        return self.id_to_str


class Movement(BaseModel):
    from_pos_x = models.IntegerField()
    from_pos_y = models.IntegerField()

    to_pos_x = models.IntegerField()
    to_pos_y = models.IntegerField()


class Chessman(BaseModel):
    class Color(models.TextChoices):
        WHITE = 'WHITE'
        BLACK = 'BLACK'

    pos_x = models.IntegerField()
    pos_y = models.IntegerField()
    type = models.CharField(max_length=32, choices=ChessType.choices())
    color = models.CharField(max_length=5, choices=Color.choices)

    movements = models.ManyToManyField(Movement)

    @property
    def board_session(self):
        return self.boardsession_set.first()

    @property
    def logic(self):
        return ChessType.logic(self.type)(chessman=self)

    def move(self, expected_x: int, expected_y: int):
        movement = Movement.objects.create(
            from_pos_x=self.pos_x,
            from_pos_y=self.pos_y,
            to_pos_x=expected_x,
            to_pos_y=expected_y
        )

        self.pos_x = expected_x
        self.pos_y = expected_y
        self.save()

        self.movements.add(movement)

        return self

class BoardSession(BaseModel):
    chessmans = models.ManyToManyField(Chessman)