from rest_framework import serializers


class OrderSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    company_id = serializers.IntegerField()
    pizza = serializers.IntegerField()
    size = serializers.CharField()
    quantity = serializers.IntegerField()
    delivery_address = serializers.IntegerField()
    total_price = serializers.FloatField()
    status = serializers.CharField()
    timestamp = serializers.DateField(read_only=True)