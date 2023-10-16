from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from swiftickets.models import *
from django.shortcuts import render

# Create your views here.

class Event(APIView):
    ''' Esta API serve para obter a relação de Eventos '''
    def get(self, request):
        return Response()
    
    def post(self, request):
        return Response()
    
    def put(self, request):
        return Response()
    
    def delete(self, request):
        return Response()
    
class Ticket(APIView):
    ''' Esta API serve para obter a relação de Ticket '''
    def get(self, request):
        return Response()