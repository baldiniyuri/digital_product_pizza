from authentication.models import User
from authentication.serializers import CredentialSerializer, UserSerializer
from address.models import Address
from core.utils import CoreUtils
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


CORE = CoreUtils()


class UserView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if CORE.check_user_exists(request):
            return Response(serializer.data, status=status.HTTP_409_CONFLICT)
        
        address = request.data.pop("address")
        address = Address.objects.create(**address)
        
        user = User.objects.create_user(address=address, username=request.data['email'], **request.data)

        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class LoginView(APIView): 
    def post(self, request):
        serializer = CredentialSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=request.data['email'], password=request.data['password'])


        if user is not None:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, user_id):
        if not CORE.find_user(user_id):
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        CORE.delete_user_token(user_id)         
        return Response(status=status.HTTP_200_OK)