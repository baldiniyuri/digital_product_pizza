from rest_framework import serializers
from address.serializers import AddressSerializers
from pizza.serializers import PizzaSerializers


class CompanySerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    cnpj = serializers.CharField()
    address = AddressSerializers()
    contact_number = serializers.CharField()
    email = serializers.EmailField()
    description = serializers.CharField()
    pizzas = PizzaSerializers(many=True)