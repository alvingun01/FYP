

from django.db import models

class Stall(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    photo = models.URLField()
    category = models.CharField(max_length=50)
    
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    stall = models.ForeignKey(Stall, on_delete=models.CASCADE, related_name='menus')
    name = models.CharField(max_length=100)
    photo = models.URLField()
    price = models.FloatField()
    category = models.CharField(max_length=50)
    hot = models.BooleanField()
    peanut = models.BooleanField(default=False)
    shrimp = models.BooleanField(default=False)
    lactose = models.BooleanField(default=False)
    halal = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    table_no = models.IntegerField()
    telp_no = models.CharField(max_length=14, null=True)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderStall(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20, default='In Progress') # In Progress, Ready for Pickup, Done
    stall = models.ForeignKey(Stall, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='stalls')

class OrderMenu(models.Model):
    order_stall = models.ForeignKey(OrderStall, on_delete=models.CASCADE, related_name='menus')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()