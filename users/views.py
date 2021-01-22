from django.contrib.auth.models import User, Group
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate

std_certificate = "11"

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class RegisterAPI(generics.CreateAPIView):
    def post(self, request):
        username, password1, password2 = request.data['username'], request.data['password1'], request.data['password2']
        
        # 아이디(핸드폰번호)
        if User.objects.filter(username=username).count() > 0:
            return Response({"message":"username exists"})
        
        # 비번(4자리)
        if password1 != password2:
            return Response({"message":"password not matching"})
        elif len(password1) != 4:
            return Response({"message":"password wrong length"})
        
        # 인증번호 없으면
        if 'certificate' not in request.data:
            return Response({"message":"no certificate"})
        # 인증번호 있는데, 일치하지 않으면
        else:
            certificate = request.data['certificate']
            if certificate != std_certificate:
                return Response({"message":"wrong certificate"})
        
        user = User.objects.create_user(
            username = username,
            password = password1
        )
        token = Token.objects.create(user=user)

        return Response({"key": token})
        

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]