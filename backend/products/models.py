from django.db import models
from autoslug import AutoSlugField 
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")

    
    def __str__(self) -> str:
        return self.name
        

class Product(models.Model):

    STATUS = (('A','available'),('U','unavailable'))

    name = models.CharField(max_length=100)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    available = models.CharField(max_length=1,choices=STATUS, default=STATUS[0])
    image = models.ImageField(upload_to="media", blank=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("products:detail", kwargs={"pk": self.id})

    def get_absolute_url(self):
        return '/products/{}/'.format(self.pk)