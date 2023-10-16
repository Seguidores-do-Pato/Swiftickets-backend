from rest_framework import serializers
from swiftickets.models import EventImage
from swiftickets.validator import ImageValidator
from drf_extra_fields.fields import Base64ImageField

class EventImageSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    img = Base64ImageField(required=True, validators=[ImageValidator()])

    class Meta:
        model = EventImage
        fields = (
            'id',
            'event',
            'img',
        )
