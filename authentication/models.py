from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, username=None, password=None):
        """
        creates a normal user
        :param email: user email
        :param username: name
        :param password: password
        :return: user object
        """
        if not email:
            raise ValueError("Email should not be empty")
        if not username:
            raise ValueError("Username should not be empty")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username=None, password=None):
        """
        Creates and returns a superuser with the given email, username, and password.
        """
        user = self.create_user(email=email, username=username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Customer(AbstractUser, PermissionsMixin):
    """
    Customer model
    """
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    phone_number = models.CharField(max_length=13)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()  # tells django how to manage customer objects

    def __str__(self):
        return self.email

