from django.db import models
from swiftickets.mixins.models import ModelBase
from swiftickets.utils import img_path

class EventImage(ModelBase):
    """
        model para adicionar imagem ao evento
    """
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='imgs')
    img = models.ImageField(max_length=100, upload_to=img_path)

    def delete(self, *args, **kwargs):
        self.img.delete()
        super(EventImage, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'event_image'
        managed = True
        verbose_name = 'EventImage'
        verbose_name_plural = 'EventImages'
        ordering = ["-created_at"]