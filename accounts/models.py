from django.db import models




from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.db.models.fields import IntegerField

from django.utils.translation import ugettext_lazy as _

# Create your models here.




class subscibers(models.Model):

    data = models.CharField(max_length=200, default="Home")
   
    
    def __str__(self):
        return self.data



class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, mobile_number, password, **extra_fields):
        """Create and save a User with the given email and password."""

        print('model number')
        print(mobile_number)
        
        user = self.model(email=email,mobile_number = mobile_number, **extra_fields)
        user.set_password(password)
        
        user.save(using=self._db)
        return user

    def create_user(self, email, mobile_number, password, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, mobile_number, password , **extra_fields)

    def create_superuser(self, mobile_number, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        email = None

        return self._create_user(email, mobile_number, password, **extra_fields)


    # code for mobile login




class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), null=True, unique=True)
    mobile_number = models.CharField(max_length= 20, null=True, unique=True)
    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = []
 
    objects = UserManager()

    ordering = ('mobile_number',)

    def __str__(self):  
        return self.mobile_number or ''

        


