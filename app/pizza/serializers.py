from rest_framework import serializers
from ingredients.serializers import IngredientsSerializers


class PizzaSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    flavor = serializers.CharField()
    second_flavor = serializers.CharField(required=False)
    is_two_flavors = serializers.BooleanField(required=False)
    is_custom = serializers.BooleanField(required=False)
    ingredients = IngredientsSerializers(many=True, required=False)