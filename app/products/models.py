from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    name = models.TextField(verbose_name='name')
    description = models.TextField(verbose_name='description')
    owner = models.ForeignKey(User)
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Time created'
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
