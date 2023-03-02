
from django.forms import ModelForm
from foodies.models import *

class StallForm(ModelForm):
    class Meta:
        model = Stall
        fields = ['name','category','photo']

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['name','price','hot','category','peanut','shrimp','lactose','halal','vegetarian','photo']

class OrderForm(ModelForm):
    class Meta:
        model = Order 
        fields = ['table_no']

class OrderMenuForm(ModelForm):
    class Meta:
        model = OrderMenu
        fields = ['quantity','notes']