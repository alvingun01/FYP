from django.urls import path
from foodies.views import *

app_name = 'foodies'

urlpatterns = [
    path('start/', start, name='start'),
    path('move-out/', move_out, name='move_out'),
    path('start/ch/', start_chinese, name='start_chinese'),
    path('', home, name='home'),
    path('ch/', home_chinese, name='home_chinese'),
    path('stall/<int:id>/', stall, name='stall'),
    path('stall/ch/<int:id>/', stall_chinese, name='stall_chinese'),
    
    path('auth/new-stall/', new_stall, name='new_stall'),
    path('auth/new-menu/<int:id>/', new_menu, name='new_menu'),
    path('auth/', admin_home, name='admin_home'),
    path('auth/stall/<int:id>/', admin_stall, name='admin_stall'),

    path('order-stall/<int:id>/', order_stall, name='order_stall'),
    
    path('api/stall/', stall_api, name='stall_api'),
    path('api/stall/<int:id>/', stall_id_api, name='stall_id_api'),
    path('api/menu/<int:id>/', menu_id_api, name='menu_id_api'),
    path('api/order/', order_api, name='order_api'),
    path('api/order/<int:id>/', order_id_api, name='order_id_api'),
    path('api/order-stall/<int:id>/', order_stall_id_api, name='order_stall_id_api'),
    path('api/order-stall/<int:order_id>/<int:stall_id>/', order_stall_api, name='order_stall_api'),
    path('api/order-menu/<int:order_stall_id>/<int:menu_id>/', order_menu_api, name='order_menu_api'),
    path('api/order-menu/v2/<int:order_id>/<int:menu_id>/', order_menu_v2_api, name='order_menu_v2_api'),
    path('api/order-menu/<int:id>/', order_menu_id_api, name='order_menu_api'),
    path('api/checkout/<int:id>/', checkout_api, name='checkout_api'),
    path('api/random/', random_api, name='random_api'),
]