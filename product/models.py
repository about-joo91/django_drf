from django.db import models
from user.models import UserModel
# Create your models here.

class Product(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    thumbnail = models.FileField(upload_to='product/')
    desc = models.TextField()
    make_date = models.DateField(auto_now_add=True)
    exposure_start_date = models.DateField()
    exposure_end_date = models.DateField()
