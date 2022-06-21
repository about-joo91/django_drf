import datetime as dt
from pytz import utc
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from rest_framework import status

class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)

class IsAdminOrAfterSevenDaysFromJoined(BasePermission):
    """
    admin유저이거나 가입한지 7일이 지난 사용자만 POST 가능
    """
    SAFE_METHODS = ('GET', )
    message = '접근 권한이 없습니다.'
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response = {
                "detail" : "서비스를 이용하기 위해 로그인 해주세요."
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED,detail=response)
        if bool(dt.datetime.now(utc) - user.join_date >= dt.timedelta(days=7)) or user.is_admin:
            return True
        if user.is_authenticated and request.method in self.SAFE_METHODS:
            return True
        return False