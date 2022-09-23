from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid

class MyAccountManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email: raise ValueError('Enter email')

		user = self.model(
			email=self.normalize_email(email),
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


# if , let's say, dad wants to add not only his fammily, but his father's family
class Family(models.Model):
	family_name = models.CharField(max_length=100)
	slug = models.SlugField(null=True, blank=True, max_length=150, unique = True,verbose_name='Link', default=str(uuid.uuid4()).replace('-',''))


class Account(AbstractBaseUser, PermissionsMixin):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	first_name				= models.CharField(max_length=50, blank=True)
	last_name				= models.CharField(max_length=50, blank=True)
	member 					= models.ForeignKey(Family,verbose_name='Family', on_delete=models.DO_NOTHING, null=True, blank=True)
	
	date_joined				= models.DateTimeField(verbose_name='Registration date', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='Last Login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	objects = MyAccountManager()

	def __str__(self):
		return self.email
	
	def get_username(self):
		return self.email.split('@')[0]
