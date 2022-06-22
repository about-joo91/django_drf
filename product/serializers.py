from django.db.models import Sum
import datetime as dt
from dateutil.tz import gettz
from rest_framework import serializers
from .models import Product, Review
# from user.models import UserModel

TODAY = dt.datetime.now(gettz('Asia/Seoul')).date()
class ReivewSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    def get_author(self, obj):
        return obj.author.username
    class Meta:
        model = Review
        fields= ["author", "content","grade","write_date"]
class ProductSerializer(serializers.ModelSerializer):
    review_info = serializers.SerializerMethodField(read_only = True)
    writer = serializers.SerializerMethodField(read_only=True)
    def get_review_info(self,obj):
        sum_of_grade = obj.review_set.aggregate(Sum('grade'))['grade__sum']
        len_of_reviews = len(obj.review_set.all())
        if len_of_reviews == 0:
            return {}
        avg_grade_of_review = int(sum_of_grade / len_of_reviews)
        first_review = obj.review_set.all().order_by('-write_date').first()
        return {
            "latest_review" : ReivewSerializer(first_review).data,
            "avg_grade" : avg_grade_of_review
        }
    def get_writer(self, obj):
        return obj.author.username
    def validate(self, data):
        
        if data.get('exposure_end_date') < TODAY:
            raise serializers.ValidationError(
                detail= {"error" : "노출 종료일이 오늘보다 이전일 수 없습니다."}
            )
        return data
    
    def create(self, validated_data):
        print(validated_data['author'])
        desc = validated_data.pop('desc')
        validated_data['desc'] = desc + f" {TODAY}에 등록된 상품입니다."
        new_product = Product(**validated_data)
        new_product.save()
        return new_product
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == 'desc':
                value = f"{TODAY} 에 수정되었습니다. " + value
            setattr(instance, key, value)
        instance.save()
        return instance
    class Meta:
        model = Product
        fields = [
            'writer','author','title','thumbnail', 'desc','review_info',
            'make_date','exposure_end_date','price',
            ]
        extra_kwargs = {"author" : {"write_only" : True}}

# class UserBaseProductSerializer(serializers.ModelSerializer):
#     products = serializers.SerializerMethodField()
#     def get_products(self,obj):
#         products = obj.product_set.all().filter(
#             exposure_end_date__gte = dt.datetime.now(gettz('Asia/Seoul')).date()
#             )
#         return [ProductSerializer(product).data for product in products]
#     class Meta:
#         model = UserModel
#         fields = ['username', 'products']
