from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import Orderserializer,Orderstatusserializer
from .models import order
from djwebhooks.decorators import hook
import asyncio
import time
from djwebhooks.models import WebhookTarget
# Create your views here.

@api_view(["POST"])
def merchent_for_pay(request):
    sera=Orderserializer(data=request.data)
    if sera.is_valid():
        ser=sera.save()
        return  Response(sera.data,status=status.HTTP_200_OK)
    return  Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def merchent_check_payment(request):
    id=request.GET['order_id']
    try:
        orders=order.objects.get(order_id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    seralizer=Orderstatusserializer(orders)
    return  Response(seralizer.data,status=status.HTTP_200_OK)
