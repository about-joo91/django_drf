from django.shortcuts import render
from .models import UserModel

from django.contrib.auth import login, authenticate, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserView(APIView):
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