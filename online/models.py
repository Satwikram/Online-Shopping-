from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not phone:
            raise ValueError('Users must have a  phone number')

        user = self.model(
            phone=self.normalize_userid(phone),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password):
        """
        Creates and saves a superuser with the given phone and password.
        """
        user = self.create_user(
            phone,
            password=password,
        )
        user.save(using=self._db)
        return user


# Create your models here.

class UserRegisteration(AbstractBaseUser):

    is_staff = models.BooleanField(default = False)
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    email = models.EmailField(verbose_name='email address',max_length=100, unique = True)
    password = models.CharField(max_length=150)
    phone = models.CharField(max_length=150,unique=True)
    verified = models.BooleanField(default = False)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True


class Otp(models.Model):

    otp = models.IntegerField()
    email = models.EmailField(verbose_name = 'email address', max_length = 100)



