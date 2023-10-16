import uuid
from django.db import models
from swiftickets.mixins.models import ModelBase
from authuser.models import User

class Event(ModelBase):
    EventType = models.TextChoices(
        "EventType",
        "Show Festival"
    )

    EventState = models.TextChoices(
        "EventState",
        "Open Closed"
    )

    EventLocal = models.TextChoices(
        "EventLocal",
        "Acre Alagoas Amapá Amazonas Bahia Ceará DistritoFederal EspíritoSanto Goiás Maranhão MatoGrosso MatoGrossodoSul MinasGerais Pará Paraíba Paraná Pernambuco Piauí RiodeJaneiro RioGrandedoNorte RioGrandedoSul Rondônia Roraima SantaCatarina SãoPaulo Sergipe Tocantins"
    )
    creater = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False)
    type = models.CharField(max_length=14, choices=EventType.choices)
    title = models.CharField(max_length=255)
    description = models.TextField()
    adress = models.CharField(max_length=255)
    uf = models.CharField(
        max_length=16, choices=EventLocal.choices, blank=True, null=True)
    state = models.CharField(
        max_length=14, choices=EventState.choices, default="Open")
    
    def __str__(self):
        return str(self.title)

    def next_state(state):
        return "Closed"

    class Meta:
        db_table = 'event'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ["-created_at"]