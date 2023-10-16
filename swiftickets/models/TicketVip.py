from django.db import models
from swiftickets.mixins.models import ModelBase
from swiftickets.models import Event

#ticket VIP
class TicketVip(ModelBase):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    num_available = models.PositiveIntegerField()
    sale_start = models.DateTimeField()
    sale_end = models.DateTimeField()

    def __str__(self):
        return f'Ticket VIP - {self.event.title}'

    class Meta:
        db_table = 'ticket_vip'
        verbose_name = 'VIPTicket'
        verbose_name_plural = 'VIPTickets'
        ordering = ["-created_at"]