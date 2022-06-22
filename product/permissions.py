import datetime as dt
from dateutil.tz import gettz
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from rest_framework import status
TODAY = dt.datetime.now(gettz('Asia/Seoul')).date()
class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)

class ProductIsAuthenticatedORAfterThreeDaysFromJoin(BasePermission):
    """
    authenticated면 조회가 가능하고 post는 3일이 지난 사용자만 가능하게 커스텀
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
        if bool(TODAY - user.join_date >= dt.timedelta(days=3)) or user.is_admin:
            return True
        if user.is_authenticated and request.method in self.SAFE_METHODS:
            return True
        return False