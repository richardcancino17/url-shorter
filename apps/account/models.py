from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, \
    AbstractBaseUser


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser,
                     **extra_fields):
        user = self.model(email=email, is_active=True,
                          is_staff=is_staff, is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


# Module to login in Django admin, just to see the url's in a dashboard

class User(AbstractBaseUser, PermissionsMixin):

    is_staff = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
