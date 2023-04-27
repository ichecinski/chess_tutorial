from rest_framework import serializers

from board.models import Chessman, BoardSession
from board.serializers.chessman import ChessmanSerializer


class BoardSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardSession
        fields = ('id',)


class BoardSessionAddChessmanSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(queryset=BoardSession.objects.all())
    chessman = ChessmanSerializer()

    def validate(self, attrs):
        validated_data = super(BoardSessionAddChessmanSerializer, self).validate(attrs)

        board_session = validated_data['id']

        chessman = validated_data['chessman']
        chessman_pos_x = chessman['pos_x']
        chessman_pos_y = chessman['pos_y']

        if board_session.chessmans.filter(pos_x=chessman_pos_x, pos_y=chessman_pos_y).exists():
            raise serializers.ValidationError(
                {'chessman': 'Chessman with given position already exists on the board.'}
            )

        return validated_data

    def create(self, validated_data):
        board_session = validated_data['id']
        chessman = Chessman.objects.create(**validated_data['chessman'])
        board_session.chessmans.add(chessman)
        return board_session

    def to_representation(self, instance):
        return BoardSessionSerializer(instance=instance).data