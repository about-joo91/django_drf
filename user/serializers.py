from rest_framework import serializers
from .models import UserModel, UserProfile, Hobby
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
    category = CategorySerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, source="comment_set", read_only=True)
    class Meta:
        model = Article
        fields = ["author","title","contents","category",
        "comments","start_of_exposed_day","end_of_exposed_day"]
        extra_kwargs = {
            'author' : {'write_only' : True}
        }
class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ['hobby_name']
class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True, read_only =True)
    get_hobbies = serializers.ListField(required = False)
    class Meta:
        model = UserProfile
        fields = ["bio", "age", "hobby", "get_hobbies"]
class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    articles = ArticleSerializer(many=True, source = "article_set", read_only= True)

    def create(self, validate_data):
        user_profile = validate_data.pop("userprofile")
        
        hobbies = user_profile.pop("get_hobbies")

        user = UserModel(**validate_data)
        user.save()

        user_profile = UserProfile.objects.create(user= user, **user_profile)

        user_profile.hobby.add(*hobbies)
        user_profile.save()
        return user
    class Meta:
        model = UserModel
        fields = ["username","password","email", "fullname", "userprofile","articles"]
    extra_kwargs = {
            'password' : {'write_only' : True}
        }