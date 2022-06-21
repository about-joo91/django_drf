import datetime as dt
from django.db import models
from user.models import UserModel
# Create your models here.
class Category(models.Model):
    cate_name = models.CharField('cate_name', max_length=128)
    desc = models.TextField()

class Article(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    title = models.CharField('title', max_length=100)
    contents = models.TextField()
    category = models.ManyToManyField('Category')
    start_of_exposed_day = models.DateField(auto_now_add=True)
    end_of_exposed_day = models.DateField(default=(dt.date.today() + dt.timedelta(days=7)))

class Comment(models.Model):
    author = models.ForeignKey(UserModel,on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey('Article',on_delete=models.CASCADE)
    contents = models.TextField()
