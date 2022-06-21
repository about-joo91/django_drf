from django.urls import path
from . import views
urlpatterns = [
    path('product',views.ProductView.as_view()),
    path('product/<int:product_id>',views.ProductView.as_view())
]
