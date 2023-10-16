from rest_framework import serializers

from core import settings


class ImageValidator:
    def __call__(self, value):
        if (settings.MAX_IMAGE_SIZE < len(value.file.getbuffer())):
            raise serializers.ValidationError(
                    'Image size must be less than 2 MB')
        return True