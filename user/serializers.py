from rest_framework import serializers
from .models import UserModel, UserProfile
from blog.models import Article, Comment,Category
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["author", "contents"]
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["cate_name"]
class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    comments = CommentSerializer(many=True, source="comment_set")
    class Meta:
        model = Article
        fields = ["title","contents","category","comments"]
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["bio", "age"]
class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    articles = ArticleSerializer(many=True, source = "article_set")
    class Meta:
        model = UserModel
        fields = ["username","email", "full_name", "userprofile","articles"]