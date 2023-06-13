from rest_framework import serializers
from company.serializers import CompanySerializers
from authentication.serializers import UserSerializer

class ReviewSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    rating = serializers.IntegerField()
    review_text = serializers.CharField()
    timestamp = serializers.DateTimeField(read_only=True)
    company_id = serializers.IntegerField(write_only=True)


class ReviewGetSerializers(ReviewSerializers):
    customer = UserSerializer()
    company = CompanySerializers()
