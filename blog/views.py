from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .models import Article
# Create your views here.

class ArticleView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        cur_user = request.user
        articles = Article.objects.filter(author = cur_user)
        titles = [article.title for article in articles]
        return Response({
            "titles" : titles
        })