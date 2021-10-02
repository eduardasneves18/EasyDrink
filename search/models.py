from django.db import models
from products.models import Product,Category

# Create your models here.
class Search(models.Model):
    title = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True,related_name="titulo")
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True,related_name="categoria")
    price = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True,related_name="preco")
    description = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True,related_name="descricao")
    image = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True,related_name="imagem")

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.title,
                                               self.category,
                                               self.price,
                                               self.description,
                                               self.title)