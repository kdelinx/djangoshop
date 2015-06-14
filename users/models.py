# coding: utf-8
from django.db import models
from core.models import AbstractClass
from users.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class User(AbstractClass, AbstractBaseUser, PermissionsMixin):
    name = models.CharField(
        'Имя',
        max_length=64,
        blank=True,
        null=True
    )
    first_name = models.CharField(
        'Фамилия',
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
        'Телефон',
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
        'Страна',
        max_length=150,
        blank=True,
        null=True
    )
    city = models.CharField(
        'Город',
        max_length=150,
        blank=True,
        null=True
    )
    index = models.CharField(
        'Индекс',
        max_length=6,
        blank=True,
        null=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'пользователь'

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return '%s - %s' % (self.first_name, self.name)

    def get_short_name(self):
        # return '%s. %s' % (self.first_name, self.name[0])
        return self.name

    def get_telephone(self):
        return self.telephone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
