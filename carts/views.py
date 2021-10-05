from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import Token
from .models import Cart, DeliveryCost
from .serializers import CartSerializer, DeliveryCostSerializer
from .helpers import CartHelper
from users.models import User 
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions
from easydrink import local_settings
import jwt


def get_id_by_token(request):
    secret_key = local_settings.SECRET_KEY
    header_token = request.META['HTTP_AUTHORIZATION'].replace('Bearer ', '')
    payload = jwt.decode(jwt=header_token, key=secret_key, algorithms=['HS256'])
    return  payload['user_id']
    

#filtro pra criar uma excessão de busca, no caso trazer itens dos carrinhos de um único usuário
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    
    userID = get_id_by_token(request)

    print('userId', userID)

    try:
        user = User.objects.get(pk=userID)
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'Error': str(e)})

    cart_helper = CartHelper(user)
    checkout_details = cart_helper.prepare_cart_for_checkout()

    if not checkout_details:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Cart of user is empty.'})

    return Response(status=status.HTTP_200_OK, data={'checkout_details': checkout_details})

    

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer

class DeliveryCostViewSet(viewsets.ModelViewSet):
    queryset = DeliveryCost.objects.all().order_by('id')
    serializer_class = DeliveryCostSerializer