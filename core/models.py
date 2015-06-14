# coding: utf-8
import uuid
from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill


def get_path_category_slider(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return 'slider/%s%s%s' % (filename[:1], filename[2:5], filename)


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


class Slider(AbstractClass):
    img = ProcessedImageField(
        upload_to=get_path_category_slider,
        format='PNG',
        options={'quality': 100},
        blank=False,
        null=False
    )
    thumbnail = ImageSpecField(
        source='img',
        processors=[ResizeToFill(1200, 480)],
        format='PNG',
        options={'quality': 100}
    )
    title = models.CharField(
        'Тайтл',
        max_length=255,
    )
    body = models.CharField(
        'Описание',
        max_length=255,
    )
    date_published = models.DateTimeField(
        'Дата публикации'
    )
    date_expired = models.DateTimeField(
        'Дата снятия с публикации'
    )
    allow_all = models.BooleanField(
        'Доступно всем',
        default=True
    )

    class Meta:
        verbose_name = u'Слайдер'
        verbose_name_plural = u'слайдер'

    def __unicode__(self):
        return self.title
