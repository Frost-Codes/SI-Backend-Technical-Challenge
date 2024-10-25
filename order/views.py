from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework import serializers

from .utils import SendSMs, SMSThread
from .models import Order
from .serializers import OrderSerializer

# Create your views here.


class OrderAPIView(generics.GenericAPIView):

    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Gets all orders for a particular customer
        :param request: django request object
        :return: All orders of a particular customer empty list if the customer has not made any orders
        """
        orders = Order.objects.filter(customer=request.user)

        serializer = self.serializer_class(orders, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Creates a new order and sends an SMS notification to the customer
        :param request: django request object
        :return: ordered item
        """

        item = request.data.get('item', '')
        amount = request.data.get('amount', '')
        phone_number = request.user.phone_number

        if phone_number == '':
            raise serializers.ValidationError('Set Your Phone number to place an order')

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(customer=request.user)

        to_send = SendSMs(f"You have ordered {item} for Ksh {amount} successfully",
                          [request.user.phone_number])

        # to_send.send()

        SMSThread(sms=to_send).start()  # using thread to send sms

        return Response(serializer.data, status=status.HTTP_201_CREATED)




