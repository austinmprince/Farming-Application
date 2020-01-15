from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

# class UserManager(BaseUserManager):


# Create your models here.
#
# class User(AbstractUser):
#     username = models.CharField(max_length=255)
#     is_farmrep = models.BooleanField(default=False)
#     is_consumer = models.BooleanField(default=True)
#     email = models.EmailField(max_length=255, unique=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=120)
#     pickups_left = models.IntegerField(default=0)
#
#     USERNAME_FIELD = 'username'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(default='')
    is_farmrep = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=120)
    pickups_left = models.IntegerField(default=0)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'
