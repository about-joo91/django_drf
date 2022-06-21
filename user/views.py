from django.shortcuts import render
from .models import UserModel, UserProfile
from django.contrib.auth import login, authenticate, logout,hashers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import UserSerializer


# Create your views here.

class UserView(APIView):
    def get(self, request):
        return Response(UserSerializer(request.user).data)

    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username= username, password = password)
        if not user:
            return Response({'error' : '존재하지 않는 계정이거나 패스워드가 일치하지 않습니다.'}, status= status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        return Response({'message': '로그인 성공!'}, status=status.HTTP_200_OK)
    def delete(self, request):
        logout(request)
        return Response({'message' : '로그아웃 성공!'}, status=status.HTTP_200_OK)

class UserControlView(APIView):
    def post(self,request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status.HTTP_200_OK)
        return Response(user_serializer.errors, status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        cur_user = request.user
        cur_user.delete()
        return Response({
            "message" : "삭제완료!"
        })