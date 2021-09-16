from rest_framework import serializers
from products.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        absolute_url = serializers.URLField(source='get_absolute_url', read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        absolute_url = serializers.URLField(source='get_absolute_url', read_only=True)
        
    my_absolute_url = serializers.SerializerMethodField() # define a SerializerMethodField        

    def get_my_absolute_url(self, obj):
        return obj.get_absolute_url() # return the absolute url of the object