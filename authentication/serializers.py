from rest_framework import serializers
from .utils import validate_number

from .models import Customer


class CustomerDetailsSerializer(serializers.ModelSerializer):
    """
    handles communication between Customer model and API views
    """

    phone_number = serializers.CharField(max_length=13, min_length=13)
    email = serializers.CharField(max_length=100, read_only=True)
    username = serializers.CharField(max_length=100, read_only=True)

    def validate(self, attrs):
        """
        validates user details from view
        :param attrs: data sent in request data
        :return: request data
        """
        phone_number = attrs.get('phone_number', '')

        valid_status, message = validate_number(number=phone_number)
        if not valid_status:
            raise serializers.ValidationError(message)

        return attrs

    class Meta:
        model = Customer
        fields = ['email', 'username', 'phone_number']


