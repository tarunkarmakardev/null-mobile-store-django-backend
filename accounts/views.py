from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        password = request.data.get('password')
        password2 = request.data.get('password2')
        if password != password2:
            return Response({'message': "Passwords don't match"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Account created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, format=None):
        user = request.user
        return Response({'current_user': user.first_name}, status=status.HTTP_200_OK)
