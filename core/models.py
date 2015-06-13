# coding: utf-8
from django.db import models


class AbstractClass(models.Model):
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    date_update = models.DateTimeField(
        auto_now=True
    )
    seo_descriptions = models.CharField(
        'SEO Descriptions',
        max_length=255,
        blank=True,
        null=True
    )


class Pages(AbstractClass):
    page = models.CharField(
        'Название страницы(en)',
        max_length=64
    )
    title = models.CharField(
        'Заголовок',
        max_length=255,
    )
    body = models.TextField(
        'Текст страницы'
    )

    class Meta:
        verbose_name = u'Статьи'
        verbose_name_plural = u'статьи'

    def __unicode__(self):
        return self.title
