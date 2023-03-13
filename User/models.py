from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class Usermanager(UserManager):
    def _create_user(self, username, fullname,  email, password, **extra_fields):
        if not email:
            raise ValueError('you must set valid email!')

        email = self.normalize_email(email)
        user = self.model(email=email,
                          username=username,
                          fullname=fullname,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)


        return user

    def create_user(self, username, email=None, fullname=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, fullname, **extra_fields)


    def create_superuser(self, username, email=None, password=None, fullname=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, fullname, **extra_fields)


class user(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, unique=True)
    fullname = models.CharField(blank=True, unique=True, max_length=120)
    username = models.CharField(blank=True, unique=True, max_length=100)
    firstname = models.CharField(blank=True, max_length=100)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password', 'fullname']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'




