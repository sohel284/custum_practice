from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import Permission


class UserManager(BaseUserManager, ):

    def get_by_natural_key(self, email):
        return self.get(email=email)

    def create_librarian(self, email, first_name, last_name, password=None, confirm_password=None):
        if not email:
            raise ValueError('librarian must have email')
        librarian = self.model(email=self.normalize_email(email),
                               first_name=first_name, last_name=last_name,
                               password=password, confirm_password=confirm_password, )
        librarian.set_password(password)
        librarian.save()
        return librarian

    def create_staffuser(self, email, first_name, last_name, password=None, confirm_password=None, ):

        if password is None:
            raise TypeError('user must have password')
        librarian = self.create_librarian(email=email, first_name=first_name,
                                          last_name=last_name, password=password, confirm_password=confirm_password, )
        librarian.is_staff = True

        librarian.save()
        return librarian

    def create_superuser(self, email, first_name, last_name, password=None, confirm_password=None, ):
        if password is None:
            raise TypeError('user must have password')
        librarian = self.create_librarian(email, first_name=first_name,
                                          last_name=last_name, password=password, confirm_password=confirm_password, )
        librarian.is_staff = True

        librarian.is_superuser = True
        librarian.is_admin = True
        librarian.save()
        return librarian


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=20, )
    last_name = models.CharField(max_length=20, )
    email = models.EmailField(max_length=255, unique=True, )
    password = models.CharField(max_length=15, )
    confirm_password = models.CharField(max_length=15, )
    is_active = models.BooleanField(default=True, )
    is_staff = models.BooleanField(default=True, )
    is_superuser = models.BooleanField(default=True, )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def natural_key(self):
        return self.first_name, self.last_name

    def __str__(self):
        return self.email


class StudentManager(BaseUserManager):
    def create_student(self, first_name, last_name, email, qualification, university, password=None,
                       confirm_password=None, ):
        if email is None:
            raise ValueError('users have must email address')
        student = Student(first_name=first_name, last_name=last_name, email=self.normalize_email(email),
                          qualification=qualification, university=university, password=password,
                          confirm_password=confirm_password, )

        student.set_password(password)

        student.save()
        return student

    objects = UserManager()


class Student(User, PermissionsMixin):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, )
    qualification = models.CharField(max_length=255, )
    university = models.CharField(max_length=50, )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'qualification', 'university', 'password', 'confirm_password', ]

    objects = StudentManager()

    def __str__(self):
        return self.first_name
