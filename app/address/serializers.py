from rest_framework import serializers


class AddressSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    city = serializers.CharField()
    state = serializers.CharField()
    postal_code = serializers.CharField()
    additional_instructions = serializers.CharField(required=False)