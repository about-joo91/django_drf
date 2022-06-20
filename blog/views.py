import json
import datetime as dt
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import Article, Category
from drf_2.permissions import IsAdminOrAfterSevenDaysFromJoined
# Create your views here.

class ArticleView(APIView):
    permission_classes = [IsAdminOrAfterSevenDaysFromJoined]
    def get(self, request):
        cur_user = request.user
        articles = Article.objects.filter(
            author = cur_user
            ).filter(
                start_of_exposed_day__lte = dt.date.today()
                ).filter(
                    end_of_exposed_day__gte = dt.date.today()
                    ).order_by('-start_of_exposed_day')
        titles = [{"title":article.title,"start_of_exposed_day":article.start_of_exposed_day, "end_of_exposed_day": article.end_of_exposed_day} for article in articles]
        return Response({
            "titles" : titles
        })
    def post(self, request):
        
        title = request.data.get('title','')
        categories = request.data.get('categories','')
        contents = request.data.get('contents','')
        categories = json.loads(categories)

        if len(title) < 6:
            return Response({
                "error": "제목이 5글자 이하면 작성할 수 없습니다."
            })
        if len(contents) < 21:
            return Response({
                "error": "내용이 20글자 이하면 작성할 수 없습니다."
            })
        if categories == '':
            return Response({
                "error": "카테고리가 비어 있습니다."
            })
        categories = [Category.objects.get(cate_name = cate_name) for cate_name in categories]
        new_article = Article.objects.create(
            author = request.user,
            title = title,
            contents = contents
        )
        new_article.category.add(*categories)
        new_article.save()
        return Response({
            "message" : "아티클 저장!"
        },status=status.HTTP_200_OK)