from rest_framework import serializers
from .models import order
from django.contrib.auth.models import User
class Userseralizer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields='__all__'

class Orderserializer(serializers.ModelSerializer):
    payment_url=serializers.SerializerMethodField(method_name='get_url')
    class Meta:
        model=order
        fields=['order_id','order_amount','payment_url']
    def get_url(self,obj):
        return 'http://127.0.0.1:8000/'

class Orderstatusserializer(serializers.ModelSerializer):
    class Meta:
        model=order
        fields=['order_id','status']