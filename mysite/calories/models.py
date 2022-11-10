

from django.contrib.auth.models import User
from django.db import models
import datetime


class UserProfile(models.Model):
    userid = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    gender = models.IntegerField(default=0)
    activity = models.FloatField(default=0)
    allowance = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        if self.gender == 0:
            self.allowance = ((10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5) * self.activity
            super().save(*args,**kwargs)
        else:
            self.allowance = ((10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161) * self.activity
            super().save(*args, **kwargs)

    def __str__(self):
        return self.userid

class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    caldj = models.IntegerField(default=0, null=False)
    protein = models.FloatField(default=0, null=False)
    fat = models.FloatField(default=0, null=False)
    carbohydrates = models.FloatField(default=0, null=False)

    def __str__(self):
        return self.name


class Visitor(models.Model):
    time_create = models.DateField(auto_now_add=True)
    userid = models.CharField(max_length=255)
    nameProduct = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, blank=True, verbose_name='Продукт')
    amount = models.IntegerField(default=0)
    caldj = models.IntegerField(default=0)
    protein = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    carbohydrates = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        self.caldj = (self.amount / 100) * Product.objects.filter(name=f'{self.nameProduct}').values('caldj')[0]['caldj']
        self.protein = (self.amount / 100) * Product.objects.filter(name=f'{self.nameProduct}').values('protein')[0]['protein']
        self.fat = (self.amount / 100) * Product.objects.filter(name=f'{self.nameProduct}').values('fat')[0]['fat']
        self.carbohydrates = (self.amount / 100) * Product.objects.filter(name=f'{self.nameProduct}').values('carbohydrates')[0]['carbohydrates']
        super().save(*args, **kwargs)


    def __str__(self):
        return self.userid



