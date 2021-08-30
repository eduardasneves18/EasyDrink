from django.db import models
from products.models import Product
from users.models import User
from django.conf import settings

# Create your models here.

class CartManager(models.Manager):

    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        queryset = self.get_queryset().filter(id = cart_id)

        if queryset.count == 1:
            new_obj = False
            cart_obj = queryset.first()
            if request.user.is_authenticate and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user = request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user = None):
        user_obj = None
        if user is not None:
            if user.is_authenticate:
                user_obj = user
        return self.model.objects.create(user = user_obj)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    products = models.ManyToManyField(Product,blank=True,null=True)
    total_price = models.DecimalField(max_digits=9,decimal_places=2,default=0.00)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    manager = CartManager()

    def __str__(self):
        return str(self.user)