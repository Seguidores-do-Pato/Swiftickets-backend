from rest_framework import serializers

from swiftickets.models import Event, EventImage
from authuser.models import User
from swiftickets.mixins.serializers import ReadOnlyModelSerializer

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'creater',
            'type',
            'title',
            'description',
            'adress',
            'uf',
            'state',
            'imgs',
            'created_at'
        )

    def to_representation(self, instance):
        from swiftickets.serializers import EventImageSerializer  # Importe aqui para evitar a importação circular
        serialized_data = super().to_representation(instance)
        serialized_data['imgs'] = EventImageSerializer(instance.imgs, many=True).data
        return serialized_data