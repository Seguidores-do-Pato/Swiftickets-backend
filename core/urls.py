from django.contrib import admin
from django.urls import path, include
from authuser.views import *
from swiftickets.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserProfile.as_view(), name="profile"),
    path('event/', Event.as_view(), name="event"),
    path('ticket/', Ticket.as_view(), name="ticket"),
]
