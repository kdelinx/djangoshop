# coding: utf-8
import uuid
from core.models import AbstractClass
from django.db import models
from users.models import User
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill


def get_path_category_pic(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return 'cat/%s%s%s' % (filename[:1], filename[2:5], filename)


def get_path_items_pic(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return 'items/%s%s%s' % (filename[:1], filename[2:5], filename)

def get_path_gallery_pic(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return 'gallery/%s%s%s' % (filename[:1], filename[2:5], filename)


class Category(AbstractClass):
    img = ProcessedImageField(
        upload_to=get_path_category_pic,
        format='PNG',
        options={'quality': 75},
        blank=True,
        null=True
    )
    preview = ImageSpecField(
        source='img',
        processors=[ResizeToFill(300, 300)],
        format='PNG',
        options={'quality': 60}
    )
    title = models.CharField(
        _('Заголовок'),
        max_length=255,
        null=False,
        blank=False
    )
    descriptions = models.TextField()

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'категории'

    def __unicode__(self):
        return self.title


class Gallery(AbstractClass):
    img = ProcessedImageField(
        upload_to=get_path_gallery_pic,
        format='PNG',
        options={'quality': 80},
        blank=True,
        null=True
    )
    preview = ImageSpecField(
        source='img',
        processors=[ResizeToFill(100, 100)],
        format='PNG',
        options={'quality': 40}
    )
    thumbnail = ImageSpecField(
        source='img',
        processors=[ResizeToFill(600, 600)],
        format='PNG',
        options={'quality': 60}
    )
    descriptions = models.CharField(
        _('Описание'),
        max_length=255,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'галерея'

    def __unicode__(self):
        return self.descriptions


class Color(AbstractClass):
    name = models.CharField(
        _('Цвет'),
        max_length=255
    )
    hex = models.CharField(
        _('hex цвета'),
        max_length=6
    )

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'цвет'

    def __unicode__(self):
        return self.name


class Sizes(AbstractClass):
    number = models.SmallIntegerField(
        _('Размеры'),
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'Размеры'
        verbose_name_plural = 'размеры'

    def __unicode__(self):
        return self.number


class Items(AbstractClass):
    title = models.CharField(
        _('Наименование'),
        max_length=255
    )
    img = ProcessedImageField(
        upload_to=get_path_items_pic,
        format='PNG',
        options={'quality': 100},
        blank=True,
        null=True
    )
    preview = ImageSpecField(
        source='img',
        processors=[ResizeToFill(300, 300)],
        format='PNG',
        options={'quality': 80}
    )
    likes = models.ManyToManyField(
        User,
        related_name='likes_user'
    )
    weight = models.DecimalField(
        _('Вес'),
        max_digits=5,
        decimal_places=2
        # max_value = 999.99
    )
    probe = models.SmallIntegerField(
        _('Проба'),
        default=0,
        null=True,
        blank=True
    )
    price = models.IntegerField(
        _('Цена')
    )
    price_per_gramm = models.SmallIntegerField(
        _('Цена за грамм'),
        default=0,
        null=True,
        blank=True
    )
    descriptions = models.TextField(
        _('Описание')
    )
    gallery = models.ManyToManyField(Gallery)
    balance = models.SmallIntegerField(
        _('Остаток'),
        default=0,
        null=False,
        blank=False
    )
    dimensions = models.CharField(
        _('Габариты'),
        max_length=64,
    )
    material = models.CharField(
        _('Материал'),
        max_length=64
    )
    color = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Sizes)
    categories = models.ForeignKey(
        Category,
        related_name='category_items'
    )

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'товары'

    def __unicode__(self):
        return self.title


class Trash(AbstractClass):
    article = models.ForeignKey(
        Items,
        related_name='article_trash'
    )
    color = models.ForeignKey(
        Color,
        related_name='color_trash'
    )
    sizes = models.ForeignKey(
        Sizes,
        related_name='sizes_trash'
    )
    count = models.SmallIntegerField(
        _('Количество товара'),
        default=0,
        null=False,
        blank=False
    )
    user = models.ForeignKey(
        User,
        related_name='trash_user'
    )
    number = models.IntegerField(
        _('Номер заказа')
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'корзина'

    def __unicode__(self):
        return '%s - %s' % (self.article.title, self.number)


class Order(AbstractClass):
    number = models.ForeignKey(
        Trash,
        related_name='number_order'
    )
    TRAVEL = (
        (0, 'Наличный расчет'),
        (1, 'Безналичный расчет'),
        (2, 'Яндекс.Деньги'),
        (3, 'Наложенный платеж'),
        (4, 'Банковская карта'),
        (5, 'WebMoney (WMR/WMZ)'),
    )
    various = models.CharField(
        _('Способ доствки'),
        choices=TRAVEL,
        max_length=64
    )
    user = models.ForeignKey(
        User,
        related_name='order_user'
    )
    date_expiries = models.DateField(
        _('Дата доставки')
    )
    address = models.CharField(
        _('Адрес доставки'),
        max_length=255,
        blank=False,
        null=False
    )
    index = models.CharField(
        _('Индекс'),
        max_length=6,
        blank=False,
        null=False
    )
    telephone = models.ForeignKey(
        User,
        related_name='telephone_user'
    )
    STATUS = (
        (0, 'Отменен'),
        (1, 'Возвращен'),
        (2, 'Завершен'),
        (3, 'В ожидании'),
        (4, 'Отгрузка'),
        (5, 'В процессе'),
        (6, 'В пути'),
    )
    status = models.CharField(
        _('Статус доставки'),
        choices=STATUS,
        max_length=16
    )

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'заказы'

    def __unicode__(self):
        return '%s - %s (%s)' % (self.number, self.status, self.various)