from rest_framework import serializers


class IngredientsSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ingredient = serializers.CharField()