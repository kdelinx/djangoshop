# coding: utf-8
import uuid
from core.models import AbstractClass
from django.db import models
from users.models import User
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill


def get_path_category_pic(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return 'category/%s%s%s' % (filename[:1], filename[2:5], filename)


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
        'Заголовок',
        max_length=255,
        null=False,
        blank=False
    )
    descriptions = models.TextField(
        'Описание'
    )

    class Meta:
        verbose_name = u'Категории'
        verbose_name_plural = u'категории'

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
        'Описание',
        max_length=255,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = u'Галерея'
        verbose_name_plural = u'галерея'

    def __unicode__(self):
        return self.descriptions


class Color(AbstractClass):
    name = models.CharField(
        'Цвет',
        max_length=255
    )
    hex = models.CharField(
        'hex цвета',
        max_length=6
    )

    class Meta:
        verbose_name = u'Цвет'
        verbose_name_plural = u'цвет'

    def __unicode__(self):
        return self.name


class Sizes(AbstractClass):
    number = models.SmallIntegerField(
        'Размеры',
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = u'Размеры'
        verbose_name_plural = u'размеры'

    def __unicode__(self):
        return '%s' % self.number


class Items(AbstractClass):
    title = models.CharField(
        'Наименование',
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
    visitors = models.IntegerField(
        'Просмотры',
        default=0,
        blank=True,
        null=True,
    )
    likes = models.ManyToManyField(
        User,
        related_name='likes_user',
        blank=True,
        null=True,
    )
    weight = models.DecimalField(
        'Вес',
        max_digits=5,
        decimal_places=2
        # max_value = 999.99
    )
    probe = models.SmallIntegerField(
        'Проба',
        default=0,
        null=True,
        blank=True
    )
    price = models.IntegerField(
        'Цена'
    )
    price_per_gramm = models.SmallIntegerField(
        'Цена за грамм',
        default=0,
        null=True,
        blank=True
    )
    descriptions = models.TextField(
        'Описание'
    )
    gallery = models.ManyToManyField(
        Gallery,
        related_name='gallery_items',
    )
    balance = models.SmallIntegerField(
        'Остаток',
        default=0,
        null=False,
        blank=False
    )
    counter_buy = models.IntegerField(
        'Количество покупок'
    )
    dimensions = models.CharField(
        'Габариты',
        max_length=64,
    )
    material = models.CharField(
        'Материал',
        max_length=64
    )
    color = models.ManyToManyField(
        Color,
        related_name='color_items',
    )
    sizes = models.ManyToManyField(
        Sizes,
        related_name='size_items',
        blank=True,
        null=True
    )
    categories = models.ForeignKey(
        Category,
        related_name='category_items',
    )

    class Meta:
        verbose_name = u'Товары'
        verbose_name_plural = u'товары'

    def __unicode__(self):
        return self.title

    def get_color(self):
        return '#%s' % self.color


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
        'Количество товара',
        default=0,
        null=False,
        blank=False
    )
    user = models.ForeignKey(
        User,
        related_name='trash_user'
    )
    number = models.IntegerField(
        'Номер заказа'
    )

    class Meta:
        verbose_name = u'Корзина'
        verbose_name_plural = u'корзина'

    def __unicode__(self):
        return '%s - %s' % (self.article.title, self.number)


class Travel(AbstractClass):
    name = models.CharField(
        'Способ доставки',
        max_length=32
    )

    class Meta:
        verbose_name = u'Способы доставки'
        verbose_name_plural = u'способы доставки'

    def __unicode__(self):
        return self.name


class Payment(AbstractClass):
    name = models.CharField(
        'Способ оплаты',
        max_length=64
    )

    class Meta:
        verbose_name = u'Способы оплаты'
        verbose_name_plural = u'способы оплаты'

    def __unicode__(self):
        return self.name


class Order(AbstractClass):
    number = models.ForeignKey(
        Trash,
        related_name='number_order'
    )
    various = models.ForeignKey(
        Payment,
        related_name='payment_order'
    )
    user = models.ForeignKey(
        User,
        related_name='order_user'
    )
    date_expiries = models.DateField(
        'Дата доставки',
    )
    address = models.CharField(
        'Адрес доставки',
        max_length=255,
        blank=False,
        null=False
    )
    index = models.CharField(
        'Индекс',
        max_length=6,
        blank=False,
        null=False
    )
    telephone = models.CharField(
        'Телефон',
        max_length=16,
    )
    status = models.ForeignKey(
        Travel,
        related_name='travel_order'
    )

    class Meta:
        verbose_name = u'Заказы'
        verbose_name_plural = u'заказы'

    def __unicode__(self):
        return '%s - %s (%s)' % (self.number, self.status, self.various)
