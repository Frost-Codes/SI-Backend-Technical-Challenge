from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):

    item = serializers.CharField(min_length=2, max_length=200)
    amount = serializers.IntegerField(min_value=1)

    def validate(self, attrs):
        """
        Validates order details against the Order model
        :param attrs: request object body data
        :return: True if data is valid else False
        """
        return attrs

    class Meta:
        model = Order
        fields = ['id', 'customer', 'item', 'amount', 'order_time']
        read_only_fields = ['customer', 'order_time']
