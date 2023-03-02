

from rest_framework import serializers
from foodies.models import *

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','name','price','hot','category','peanut','shrimp','lactose','halal','vegetarian','photo']

class StallSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = Stall
        fields = ['id','name','menus','category','photo']

class SimpleStallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stall
        fields = ['id','name','category','photo']

class OrderMenuSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(read_only=True)

    class Meta:
        model = OrderMenu
        fields = ['id','menu','quantity','notes']

class OrderStallSerializer(serializers.ModelSerializer):
    menus = OrderMenuSerializer(many=True, read_only=True)
    stall = SimpleStallSerializer(read_only=True)

    class Meta: 
        model = OrderStall
        fields = ['id','status','stall','menus']

class OrderSerializer(serializers.ModelSerializer):
    stalls = OrderStallSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id','table_no','telp_no','paid','stalls','created_at']