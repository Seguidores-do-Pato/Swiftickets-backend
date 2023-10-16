import uuid
from django.db import models

class ModelBase(models.Model):
    """
        Modelo base que reune atributos comuns aos modelos

        active = Se o registro está ativo
        created_at = Criação do registro
        updated_at = Última atualização
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]