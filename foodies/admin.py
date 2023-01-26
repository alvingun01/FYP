from django.contrib import admin
from foodies.models import *

admin.site.register(Stall)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderStall)
admin.site.register(OrderMenu)