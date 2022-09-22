from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid

class MyAccountManager(BaseUserManager):
	def create_user(self, email, password=None, phone_number=None):
		if not email: raise ValueError('Enter email')

		user = self.model(
			email=self.normalize_email(email),
			phone_number=phone_number,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser, PermissionsMixin):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	first_name				= models.CharField(max_length=30, default='', blank=True)
	last_name				= models.CharField(max_length=30, default='', blank=True)
	
	date_joined				= models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='Последний вход', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	objects = MyAccountManager()

	def __str__(self):
		return self.email
	