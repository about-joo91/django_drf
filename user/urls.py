from django.urls import path
from user import views
urlpatterns = [
    path('user',views.UserView.as_view()),
    path('user_control',views.UserControlView.as_view())
]
