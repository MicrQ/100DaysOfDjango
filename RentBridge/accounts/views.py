""" views for account related endpoints """
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import Token
from .serializers import UserRegistrationSerializer, UserLoginSerializer


class UserRegistrationView(APIView):
    """ api veiw for user registration """
    def post(self, request):
        """ used to create a new user """
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {'message': 'User registered successfully',
                 'token': token.key},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    """ api view for login """
    def post(self, request):
        """ used to login a user """
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    'message': 'Logged in successfully',
                    'token': token.key
                },
                status=status.HTTP_200_OK)
        return Response(
            {
                'error': 'Invalid credentials'
            },
            status=status.HTTP_401_UNAUTHORIZED)
