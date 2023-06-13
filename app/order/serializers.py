from rest_framework import serializers
from authentication.serializers import UserSerializer
from company.serializers import CompanySerializers
from pizza.serializers import PizzaSerializers
from address.serializers import AddressSerializers


class OrderSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    company_id = serializers.IntegerField(write_only=True)
    pizzas_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    size = serializers.CharField()
    quantity = serializers.IntegerField()
    delivery_address_id = serializers.IntegerField(write_only=True)
    total_price = serializers.FloatField()
    status = serializers.CharField()
    timestamp = serializers.DateTimeField(read_only=True)


class OrderGetSerializers(serializers.Serializer):
    customer = UserSerializer()
    company = CompanySerializers()
    pizzas = PizzaSerializers(many=True)
    delivery_address = AddressSerializers()

