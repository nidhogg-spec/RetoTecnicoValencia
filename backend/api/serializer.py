from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)
        token['nombre'] = user.nombre
        token['usuario'] = user.usuario
        token['rol'] = user.rol
        token['detalle'] = user.detalle

        return token
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only = True, required=True, validators=[validate_password]
    )
    class Meta:
        model = User
        fields = ('nombre','contraseña','usuario','rol','detalle')

    def create(self, validated_data):
        user = User.objects.create()
        user.set_password(validated_data['password'])
        user.save()
        
        return user
