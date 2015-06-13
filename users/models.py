# coding: utf-8
from django.db import models
from core.models import AbstractClass
from users.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class User(AbstractClass, AbstractBaseUser, PermissionsMixin):
    login = models.CharField(
        _('Login'),
        max_length=255,
        null=False,
        blank=False,
        unique=True
    )
    name = models.CharField(
        _('Name'),
        max_length=64,
        blank=True,
        null=True
    )
    first_name = models.CharField(
        _('First name'),
        max_length=64,
        blank=True,
        null=True
    )
    email = models.EmailField(
        _('E-mail'),
        max_length=150,
        unique=True
    )
    telephone = models.CharField(
        _('Telephone'),
        max_length=16,
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        default=True
    )

    is_admin = models.BooleanField(
        default=True
    )
    country = models.CharField(
        _('Country'),
        max_length=150,
        blank=True,
        null=True
    )
    city = models.CharField(
        _('Town'),
        max_length=150,
        blank=True,
        null=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'пользователь'

    def __unicode__(self):
        return self.login

    def get_full_name(self):
        return '%s - %s' % (self.first_name, self.name)

    def get_short_name(self):
        # return '%s. %s' % (self.first_name, self.name[0])
        return self.login

    def get_telephone(self):
        return self.telephone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin