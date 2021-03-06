from django.db.models import Q
from django.db import models
from autoslug import AutoSlugField 
from django.urls import reverse


# Criando modelo da categoria dos produtos
class Category(models.Model):
    title = models.CharField(max_length=255, null=False)
    parent_category_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    class Meta:
        ordering = ("title",)
        verbose_name = "category"
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
       return reverse("products:list_by_category", kwargs={"slug": self.slug})


# classe para trazer os produtos referentes a busca do cliente         
class ProductQuerySet(models.query.QuerySet):

    def available(self): # função para produtos disponiveis
        return self.filter(available = True)

    def featured(self): # função dos produtos em destaque.
        return self.filter(featured = True, available = True)
    
    def search(self, query):
        lookups = (Q(title__icontains = query) | # na linha 38/39 esta dizendo que o usuário quando digitar algo na search
                    Q(description__icontains = query)) # ele irá fazer uma busc pelo nome e pelas palavras da descrição do produto.
        return self.filter(lookups).distinct()


class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self.db)

    def all(self):
       return self.get_queryset().available()

    def featured(self):
        return self.get_queryset().featured()
        
    def search(self,query):
        return self.get_queryset().available().search(query)


#Criando o modelo dos produtos
class Product(models.Model):

    title = models.CharField(max_length=255, null=False)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    old_price = models.DecimalField(max_digits=9,decimal_places=2, default= 89.25)
    available = models.BooleanField(default= False)
    image = models.ImageField(upload_to="media", blank=True)
    featured = models.BooleanField(default = False)
    quantity = models.IntegerField()

    Objects = ProductManager()
    objects = ProductManager()

    class Meta: 
        ordering = ("title",)
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/products/{}/'.format(self.pk)