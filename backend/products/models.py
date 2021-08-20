from django.db import models
from autoslug import AutoSlugField 

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")

    
    def __str__(self) -> str:
        return self.name
        

class Product(models.Model):

    STATUS = (('A','available'),('U','unavailable'))
    COLORS = (
        ('#FFFFFF','WHITE'),
        ('#000000','BLACK'),
        ('#FF0000', 'RED'),
        ('#006600','GREEN'),
        ('#0033CC','BLUE'),
        ('#FFCC00', 'YELLOW'),
        ('#FF9900','ORANGE'),
        ('#9900FF','PURPLE'),
        ('#FF99CC','PINK'),
    )

    name = models.CharField(max_length=100)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    color = models.CharField(max_length = 25, choices=COLORS)
    available = models.CharField(max_length=1,choices=STATUS, default=STATUS[0])
    image = models.ImageField()
    department = models.CharField(max_length = 50)

    def __str__(self):
        return self.name