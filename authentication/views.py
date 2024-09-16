from django.shortcuts import render, redirect
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth import logout


from .serializers import CustomerDetailsSerializer


# Create your views here.

@api_view(['GET'])
def google_authentication(request):
    """
    Initiates google OAuth
    :param request: django request object
    :return: redirects user to accounts.google to authorize sign up / sign in
    """
    return redirect('social:begin', backend='google-oauth2')


class LogoutView(APIView):
    """
    Logout a customer
    """
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def post(request):
        """
        Initiates logout using django's built in logout method
        :param request: django request object
        :return: Response object
        """
        logout(request)
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_302_FOUND)


class CustomerDetailsAPIView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomerDetailsSerializer

    @staticmethod
    def get(request):
        """
        Fetches user details
        :param request: django request object
        :return: Response object of user email, username, first_name, last_name and phone_number
        """
        user = request.user

        data = {
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone_number': user.phone_number
        }

        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request):
        """
        Update user phone number
        :param request: django request object
        :return: Response object of user email, username and phone_number
        """
        customer = request.user  # get the authenticated user
        serializer = self.serializer_class(customer,  data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()  # Save the changes

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)



