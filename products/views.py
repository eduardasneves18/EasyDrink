
from django.http import Http404
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions


#filtro pra criar uma excessão de busca, no caso trazer itens de uma categoria específica
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_products_by_category(request, cat):
    products = Product.objects.filter(category=cat)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
  permission_classe = [permissions.IsAuthenticated]
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

  def get_queryset(self):
    categories = Category.objects.all()
    return categories

class ProductViewSet(viewsets.ModelViewSet):
  permission_classe = [permissions.IsAuthenticated]
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  

  def get_queryset(self):
    products = Product.objects.all()
    return products


"""
Nesta area irei adicionar as funções que farão a pesquisa do nosso site.
"""
