import datetime as dt
from dateutil.tz import gettz
from rest_framework import serializers
from .models import Product
from user.models import UserModel


class ProductSerializer(serializers.ModelSerializer):
    def validate(self, data):
        today = dt.datetime.now(gettz('Asia/Seoul')).date()
        if data.get('exposure_start_date') < today:
            raise serializers.ValidationError(
                detail= {"error" : "노출 시작일은 오늘부터 가능합니다."}
            )
        return data
    
    def create(self, validated_data):
        new_product = Product(**validated_data)
        new_product.save()
        return new_product
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    class Meta:
        model = Product
        fields = [
            'author','title','thumbnail', 'desc',
            'make_date','exposure_start_date','exposure_end_date'
            ]

class UserBaseProductSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    def get_products(self,obj):
        products = obj.product_set.all().filter(
            exposure_start_date__lte = dt.datetime.now(gettz('Asia/Seoul')).date(),
            exposure_end_date__gte = dt.datetime.now(gettz('Asia/Seoul')).date()
            )
        return [ProductSerializer(product).data for product in products]
    class Meta:
        model = UserModel
        fields = ['username', 'products']
