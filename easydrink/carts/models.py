from django.db import models
from products.models import Product
from users.models import User
from django.conf import settings

# Create your models here.

class SaleProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    amount = models.IntegerField()
    unit_price = models.DecimalField(max_digits=9,decimal_places=2,default=0.00)
    total_price = models.DecimalField(max_digits=9,decimal_places=2,default=0.00)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    products = models.ManyToManyField(SaleProduct,blank=True,null=True)
    total_price = models.DecimalField(max_digits=9,decimal_places=2,default=0.00)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)