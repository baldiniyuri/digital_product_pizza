from rest_framework import serializers


class PizzaSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    flavor = serializers.CharField()
    second_flavor = serializers.CharField(required=False)
    is_two_flavors = serializers.BooleanField(required=False)