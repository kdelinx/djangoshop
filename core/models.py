from django.db import models


class AbstractClass(models.Model):
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    date_update = models.DateTimeField(
        auto_now=True
    )