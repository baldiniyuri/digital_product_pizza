from rest_framework import serializers


class ReviewSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    customer = serializers.IntegerField()
    rating = serializers.IntegerField()
    review_text = serializers.CharField()
    timestamp = serializers.DateTimeField(read_only=True)
    pizza = serializers.IntegerField()
    company = serializers.IntegerField()
