from django.db import models
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('user.UserModel', on_delete=models.SET_NULL, null=True)
    thumbnail = models.FileField(upload_to='product/')
    desc = models.TextField()
    make_date = models.DateField(auto_now_add=True)
    exposure_end_date = models.DateField()
    price = models.IntegerField()
    edit_date = models.DateField(auto_now=True)
    is_active= models.BooleanField(default = True)

class Review(models.Model):
    author = models.ForeignKey('user.Usermodel', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    content = models.TextField()
    grade = models.IntegerField()
    write_date = models.DateField(auto_now_add=True)

