from rest_framework import serializers
from address.serializers import AddressSerializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    cpf = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField()
    address = AddressSerializers()


class CredentialSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
