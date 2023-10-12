from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.shortcuts import render

# Create your views here.

class UserProfile(APIView):
    ''' Esta API serve para obter a relação de usuários '''
    def get(self, request):
        output = [{"email":output.email, "name":output.name}
                  for output in User.objects.all()]
        return Response(output)