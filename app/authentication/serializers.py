from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    cpf = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField()


class CredentialSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)