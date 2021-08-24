from django.db import models
from django.urls import reverse

class Product():
    def get_absolute_url(self):
        print('self -> ', self)
        return reverse("products:detail", kwargs={"pk": '1'})
