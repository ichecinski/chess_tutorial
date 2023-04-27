from rest_framework import serializers

from board.models import Chessman


class ChessmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chessman
        fields = ('pos_x', 'pos_y', 'type', 'color')


class ChessmanMoveSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Chessman.objects.all())
    pos_x = serializers.IntegerField()
    pos_y = serializers.IntegerField()

    def validate(self, attrs):
        validated_data = super(ChessmanMoveSerializer, self).validate(attrs)

        chessman = validated_data['id']
        pos_x, pos_y = validated_data['pos_x'], validated_data['pos_y']

        if chessman.board_session is None:
            raise serializers.ValidationError({'board': 'Chessman is not assigned to BoardSession.'})

        if chessman.logic.is_movement_overlapping_with_other_chessman(expected_x=pos_x, expected_y=pos_y):
            raise serializers.ValidationError({'invalid_movement': 'Cannot move because it overlaps with another chessman.'})

        if chessman.logic.is_movement_allowed(expected_x=pos_x, expected_y=pos_y) is False:
            raise serializers.ValidationError({'invalid_movement': 'Prohibited movement.'})

        return validated_data

    def create(self, validated_data):
        chessman = validated_data['id']
        chessman.move(expected_x=validated_data['pos_x'], expected_y=validated_data['pos_y'])
        return chessman