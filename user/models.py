from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,username, password=None):
        if not username:
            raise ValueError('아이디가 공란이어서 곤란합니다.')
        user = self.model(
            username = username
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self, username, password=None):
        user =self.create_user(
            username= username,
            password= password
        )
        user.is_admin = True
        user.save(using= self._db)
        return user
    
# Create your models here.
class UserModel(AbstractBaseUser):
    username = models.CharField('username' , max_length=20, unique=True)
    password  = models.CharField('password', max_length=128)
    email = models.EmailField('email',max_length=128)
    fullname = models.CharField('fullname', max_length=20)
    
    join_date = models.DateTimeField('created_at', auto_now_add=True)
    updated_at = models.DateField('updated_at', auto_now=True)

    is_active = models.BooleanField(default=True)

    is_admin =models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class UserProfile(models.Model):
    user = models.OneToOneField('UserModel', on_delete=models.CASCADE)
    bio = models.TextField()
    age = models.IntegerField()
    hobby = models.ManyToManyField('Hobby')


class Hobby(models.Model):
    hobby_name = models.CharField(max_length=30)