from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['birthday'] = user.birthday
        
        return token
    
class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(), message="Esse email já está em uso. Por favor, tente novamente.")]
    )
    # birthday = serializers.DateField(format="%Y-%m-%d")
    
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    