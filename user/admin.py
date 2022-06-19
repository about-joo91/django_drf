from django.contrib import admin
from .models import UserModel,UserProfile
# Register your models here.
admin.site.register(UserModel)
admin.site.register(UserProfile)