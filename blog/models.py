from django.db import models
from user.models import UserModel
# Create your models here.
class Category(models.Model):
    cate_name = models.CharField('cate_name', max_length=128)
    desc = models.TextField()

class Article(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    title = models.CharField('title', max_length=100)
    content = models.TextField()
    category = models.ManyToManyField('Category')


