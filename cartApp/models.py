from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    name = models.CharField(verbose_name=u'название', max_length=32)
    description = models.TextField(verbose_name=u'описание', blank=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(verbose_name=u'название', max_length=32, unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name=u'название', max_length=32)
    count = models.PositiveIntegerField(verbose_name=u'количество', default=0)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    cart = models.ForeignKey(Cart, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
