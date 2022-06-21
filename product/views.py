import datetime as dt
from dateutil.tz import gettz
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from .serializers import ProductSerializer,UserBaseProductSerializer
from .models import Product
# Create your views here.
TODAY = dt.datetime.now(gettz('Asia/Seoul')).date()
class ProductView(APIView):
    def get(self, request):
        user = request.user
        # products = Product.objects.filter(
        #     Q(exposure_start_date__lte = TODAY, exposure_end_date = TODAY) |
        #     Q(author = user)
        # )
        # return Response(ProductSerializer(products, many=True).data, status=status.HTTP_200_OK)
        return Response(UserBaseProductSerializer(user).data, status=status.HTTP_200_OK)    
    def post(self, request):
        user = request.user
        request.data['author'] = user.id
        product_serializer = ProductSerializer(data = request.data)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return Response(product_serializer.data, status.HTTP_200_OK)
    def put(self,request,product_id):
        product = Product.objects.get(id = product_id)
        product_serializer = ProductSerializer(product , data = request.data, partial=True)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return Response(product_serializer.data, status.HTTP_200_OK)
    def delete():
        return Response({})
