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
    def validate(self ,data):
        if len(data.get('title') )< 6:
            raise serializers.ValidationError(
                detail= {
                    "error" : "제목이 5글자 이하면 작성할 수 없습니다."
                }
            )
        if len(data.get('contents')) < 21:
            raise serializers.ValidationError(
                detail= {
                    "error" : "내용이 20글자 이하면 작성할 수 없습니다."
                }
            )
        if data.get('category','') =='':
            raise serializers.ValidationError(
                detail= {
                    "error": "카테고리가 비어있습니다."
                }
            )
        return data
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
        password = validate_data.pop("password")
        user_profile = validate_data.pop("userprofile")
        
        hobbies = user_profile.pop("get_hobbies")

        user = UserModel(**validate_data)
        user.set_password(password)
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