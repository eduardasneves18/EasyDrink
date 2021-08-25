from django.db import models
from autoslug import AutoSlugField 
from django.urls import reverse


# Criando modelo da categoria dos produtos
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.AutoSlugField(unique=True, always_update=False, populate_from="name")
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse("products:list_by_category", kwargs={"slug": self.slug})


# Criando classe que filtrará os produtos disponiveis
class AvailableManager(models.Manager):
    def get_queryset(self):
        return super(AvailableManager,self).get_queryset().filter(available="A")
        

#Criando o modelo dos produtos
class Product(models.Model):

    STATUS = (('A','available'),('U','unavailable'))

    name = models.CharField(max_length=100)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    available = models.CharField(max_length=1,choices=STATUS)
    image = models.ImageField(upload_to="media", blank=True)

    class Meta: 
        ordering = ("name",)
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("products:detail", kwargs={"pk": self.id})

    def get_absolute_url(self):
        return '/products/{}/'.format(self.pk)