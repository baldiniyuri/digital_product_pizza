from rest_framework import serializers


class IngredientsSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ingredient_name = serializers.CharField()
    user_id = serializers.IntegerField(write_only=True)

class IngredientsAddSerializers(IngredientsSerializers):
    user_id = serializers.IntegerField(required=False)