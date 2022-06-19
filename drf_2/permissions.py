import datetime as dt
from pytz import utc
from rest_framework.permissions import BasePermission

class IsAfterThreeDaysFromJoined(BasePermission):
    """
    가입한지 3일이 지난 사용자만 가능
    """

    def has_permission(self, request, view):
        return bool(dt.datetime.now(utc) - request.user.created_at >= dt.timedelta(days=3))