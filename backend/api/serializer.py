from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)
        token['nombre'] = user.nombre
        token['username'] = user.username
        token['rol'] = user.rol
        token['descripccion'] = user.descripccion

        return token
        
class RegisterSerializer(serializers.ModelSerializer):
    contraseña = serializers.CharField(
        write_only = True, required=True, validators=[validate_password]
    )

    class Meta:
        model = CustomUser
        fields = ('nombre','contraseña','username','rol','descripccion',)

    def create(self, validated_data):

        user = CustomUser.objects.create(
            username=validated_data['username'],
            nombre=validated_data['nombre'],
            rol=validated_data['rol'],
            descripccion=validated_data['descripccion']
        )
        user.set_password(validated_data['contraseña'])
        user.save()
        
        return user
