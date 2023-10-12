from django.contrib import admin
from django.urls import path, include
from authuser.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserProfile.as_view(), name="profile")
]
