import random
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from foodies.models import *
from foodies.forms import *
from foodies.serializers import *
import time
import os, sys 
# import win32print

def start(request):
    return render(request, 'start.html')

def move_out(request):
    return render(request, 'move-out.html')

def start_chinese(request):
    return render(request, 'start-ch.html')

def home(request):
    return render(request, 'home.html')

def home_chinese(request):
    return render(request, 'home-ch.html')

def stall(request, id):
    context = { 'stall_id': id }
    return render(request, 'stall.html', context)

def stall_chinese(request, id):
    context = { 'stall_id': id }
    return render(request, 'stall-ch.html', context)

def new_stall(request):
    return render(request, 'new_stall.html')

def new_menu(request, id):
    context = { 'stall_id': id }
    return render(request, 'new_menu.html', context)

def admin_home(request):
    return render(request, 'admin_home.html')

def admin_stall(request, id):
    context = { 'stall_id': id }
    return render(request, 'admin_stall.html', context)

def order_stall(request, id):
    context = { 'stall_id': id }
    return render(request, 'order_stall.html', context)

@api_view(['GET','POST'])
def stall_api(request):
    def get():
        # Get all stalls
        stalls = Stall.objects.all()
        stalls_serialized = StallSerializer(instance=stalls, many=True)
        return Response(stalls_serialized.data, status=status.HTTP_200_OK)

    def post():
        # Create new stall
        form = StallForm(request.POST)
        if (form.is_valid()):
            new_stall = Stall.objects.create(
                name = form.cleaned_data.get('name'),
                category = form.cleaned_data.get('category'),
                photo = form.cleaned_data.get('photo'),
            )
            new_stall_serialized = StallSerializer(instance=new_stall)
            return Response(new_stall_serialized.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if (request.method == 'GET'): return get()
    elif (request.method == 'POST'): return post()

@api_view(['GET','PUT','DELETE'])
def stall_id_api(request, id):
    def get():
        # Get details of stall :id
        stall = Stall.objects.get(id=id)
        stall_serialized = StallSerializer(instance=stall)
        return Response(stall_serialized.data, status=status.HTTP_200_OK)

    def put():
        # Edit stall :id
        pass

    def delete():
        # Delete stall :id
        stall = Stall.objects.get(id=id)
        stall.delete()
        return Response(status=status.HTTP_200_OK)

    if (request.method == 'GET'): return get()
    elif (request.method == 'PUT'): return put()
    elif (request.method == 'DELETE'): return delete()

@api_view(['GET','POST'])
def menu_id_api(request, id):
    def get():
        # Get details of menu :id
        menu = Menu.objects.get(id=id)
        menu_serialized = MenuSerializer(instance=menu)
        return Response(menu_serialized.data, status=status.HTTP_200_OK)

    def post():
        # Create new menu to stall :id
        stall = Stall.objects.get(id=id)
        if (stall != None):
            form = MenuForm(request.POST)
            if (form.is_valid()):
                new_menu = Menu.objects.create(
                    stall = stall,
                    name = form.cleaned_data.get('name'),
                    price = form.cleaned_data.get('price'),
                    hot = form.cleaned_data.get('hot'),
                    category = form.cleaned_data.get('category'),
                    peanut = form.cleaned_data.get('peanut'),
                    shrimp = form.cleaned_data.get('shrimp'),
                    lactose = form.cleaned_data.get('lactose'),
                    halal = form.cleaned_data.get('halal'),
                    vegetarian = form.cleaned_data.get('vegetarian'),
                    photo = form.cleaned_data.get('photo'),
                )
                new_menu_serialized = MenuSerializer(instance=new_menu)
                return Response(new_menu_serialized.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete():
        # Delete menu :id
        menu = Menu.objects.get(id=id)
        menu.delete()
        return Response(status=status.HTTP_200_OK)

    if (request.method == 'GET'): return get()
    elif (request.method == 'POST'): return post()
    elif (request.method == 'DELETE'): return delete()

@api_view(['POST'])
def order_api(request):
    def post():
        # Create new order 
        form = OrderForm(request.POST)
        if (form.is_valid()):
            form.save()
            new_order = form.instance
            new_order_serialized = OrderSerializer(instance=new_order)
            return Response(new_order_serialized.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if (request.method == 'POST'): return post()

@api_view(['GET'])
def order_id_api(request, id):
    def get():
        # Get order cart :id
        order = Order.objects.get(id=id)
        order_serialized = OrderSerializer(instance=order)
        return Response(order_serialized.data, status=status.HTTP_200_OK)

    if (request.method == 'GET'): return get()

@api_view(['GET'])
def order_stall_api(request, order_id, stall_id):
    def get():
        # Create new order stall
        stall = Stall.objects.get(id=stall_id)
        order = Order.objects.get(id=order_id)
        if (stall != None and order != None):
            prev_order_stall = OrderStall.objects.filter(stall=stall, order=order)
            if (len(prev_order_stall) == 0):
                new_order_stall = OrderStall.objects.create(
                    stall = stall, 
                    order = order
                )
                new_order_stall_serialized = OrderStallSerializer(instance=new_order_stall)
                return Response(new_order_stall_serialized.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if (request.method == 'GET'): return get()

@api_view(['GET','PUT'])
def order_stall_id_api(request, id):
    def get():
        # Get all orders for stall :id
        stall = Stall.objects.get(id=id)
        orders = OrderStall.objects.filter(stall=stall)
        orders_serialized = OrderStallSerializer(instance=orders, many=True)
        return Response(orders_serialized.data, status=status.HTTP_200_OK)

    def put():
        # Change order stall :id status
        order = OrderStall.objects.get(id=id)
        if (order.status != 'Done'):
            if (order.status == 'In Progress'): order.status = 'Ready for Pickup'
            elif (order.status == 'Ready for Pickup'): order.status = 'Done'
            order.save()
            order_serialized = OrderStallSerializer(instance=order)
            return Response(order_serialized.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        

    if (request.method == 'GET'): return get()
    elif (request.method == 'PUT'): return put()

@api_view(['POST'])
def order_menu_api(request, order_stall_id, menu_id):
    def post():
        # Add menu :menu_id to order stall :order_stall_id
        form = OrderMenuForm(request.POST)
        if (form.is_valid()):
            order_stall = OrderStall.objects.get(id=order_stall_id)
            menu = Menu.objects.get(id=menu_id)
            if (order_stall != None and menu != None):
                prev_order_menu = OrderMenu.objects.filter(
                    order_stall = order_stall,
                    menu = menu
                )
                if (len(prev_order_menu) == 0):
                    new_order_menu = OrderMenu.objects.create(
                        order_stall = order_stall,
                        menu = menu,
                        quantity = form.cleaned_data.get('quantity'),
                        notes = form.cleaned_data.get('notes'),
                    )
                    new_order_menu_serialized = OrderMenuSerializer(instance=new_order_menu)
                    return Response(new_order_menu_serialized.data, status=status.HTTP_201_CREATED)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if (request.method == 'POST'): return post()

@api_view(['POST'])
def order_menu_v2_api(request, order_id, menu_id):
    def post():
        # Add menu :menu_id to order stall :order_stall_id
        form = OrderMenuForm(request.POST)
        if (form.is_valid()):
            menu = Menu.objects.get(id=menu_id)
            order = Order.objects.get(id=order_id)
            if (order != None and menu != None):
                order_stall = OrderStall.objects.filter(stall=menu.stall, order=order)
                if (len(order_stall) == 0):
                    order_stall = OrderStall.objects.create(stall=menu.stall, order=order)
                else:
                    order_stall = order_stall[0]
                prev_order_menu = OrderMenu.objects.filter(
                    order_stall = order_stall,
                    menu = menu
                )
                if (len(prev_order_menu) == 0):
                    new_order_menu = OrderMenu.objects.create(
                        order_stall = order_stall,
                        menu = menu,
                        quantity = form.cleaned_data.get('quantity'),
                        notes = form.cleaned_data.get('notes'),
                    )
                    new_order_menu_serialized = OrderMenuSerializer(instance=new_order_menu)
                    return Response(new_order_menu_serialized.data, status=status.HTTP_201_CREATED)
                else:
                    # print('HEREs', prev_order_menu[0].id)
                    order_menu = OrderMenu.objects.get(id=prev_order_menu[0].id)
                    form = OrderMenuForm(request.POST)
                    if (form.is_valid() and order_menu != None):
                        # print('HEREs')
                        order_menu.quantity = form.cleaned_data.get('quantity')
                        if (order_menu.quantity == 0):
                            OrderMenu.objects.get(id=prev_order_menu[0].id).delete()
                        else:
                            order_menu.save()
                        order_menu_serialized = OrderMenuSerializer(instance=order_menu)
                        return Response(order_menu_serialized.data, status=status.HTTP_200_OK)
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if (request.method == 'POST'): return post()

@api_view(['GET','PUT'])
def order_menu_id_api(request, id):
    def get():
        # Get order menu :id
        order_menu = OrderMenu.objects.get(id=id)
        order_menu_serialized = OrderMenuSerializer(instance=order_menu)
        return Response(order_menu_serialized.data, status=status.HTTP_200_OK)

    def put():
        # Edit order menu :id
        order_menu = OrderMenu.objects.get(id=id)
        form = OrderMenuForm(request.POST)
        if (form.is_valid() and order_menu != None):
            order_menu.quantity = form.cleaned_data.get('quantity')
            order_menu.notes = form.cleaned_data.get('notes')
            if (order_menu.quantity == 0):
                OrderMenu.objects.get(id=id).delete()
            else:
                order_menu.save()
            order_menu_serialized = OrderMenuSerializer(instance=order_menu)
            return Response(order_menu_serialized.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if (request.method == 'GET'): return get()
    elif (request.method == 'PUT'): return put()

@api_view(['GET'])
def checkout_api(request, id):
    def get():
        # Checkout (pay) order :id
        order = Order.objects.get(id=id)
        order.paid = True
        order.save()
        OrderStall.objects.filter(order_id=id, menus__isnull=True).delete()
        order_serialized = OrderSerializer(instance=order)

        # Print receipt
        def truncate(str, max_length):
            if (len(str) <= max_length): return str
            return f"{str[:max_length-3]}..."
        
        receipt = f"\n\n\n\n{'='*33}\n\n{'RECEIPT':^33}\n\n"
        total = 0
        for order_stall in order_serialized.data['stalls']:
            receipt += f"{order_stall['stall']['name']}\n"
            for order_menu in order_stall['menus']:
                total += order_menu['quantity']*order_menu['menu']['price']
                receipt += f"  {order_menu['quantity']:>2}x {truncate(order_menu['menu']['name'],20):20} ${order_menu['quantity']*order_menu['menu']['price']:>6.2f}\n"
        receipt += f"\n\n{'Total':26} ${total:>6.2f}\n\n{'='*33}\n"
        receipt = bytes(receipt, 'utf-8')

        # p = win32print.OpenPrinter("___") # TODO: Insert printer's name
        # job = win32print.StartDocPrinter(p, 1, ("test of raw data", None, "RAW")) 

        # for order_stall in order_serialized.data['stalls']:
        #     win32print.StartPagePrinter(p)
        #     win32print.WritePrinter(p, receipt)
        #     win32print.EndPagePrinter(p)
        #     time.sleep(4)
        #     # TODO: Stall some time to take the copy

        return Response(order_serialized.data, status=status.HTTP_200_OK)

    if (request.method == 'GET'): return get()

@api_view(['GET'])
def random_api(request):
    def get():
        # Get random menu satisfied requirements
        min_price = float(request.GET.get('minPrice'))
        max_price = float(request.GET.get('maxPrice'))
        category = request.GET.get('category')
        hot, vegetarian, halal, peanut, shrimp, lactose = None, None, None, None, None, None
        if (request.GET.get('hot') != None):
            hot = request.GET.get('hot') == 'true'
        if (request.GET.get('vegetarian') != None):
            vegetarian = request.GET.get('vegetarian') == 'true'
        if (request.GET.get('halal') != None):
            halal = request.GET.get('halal') == 'true'
        if (request.GET.get('peanut') != None):
            peanut = request.GET.get('peanut') == 'true'
        if (request.GET.get('shrimp') != None):
            shrimp = request.GET.get('shrimp') == 'true'
        if (request.GET.get('lactose') != None):
            lactose = request.GET.get('lactose') == 'true'

        def filter_menu(menu):
            return (
                min_price <= menu['price'] and menu['price'] <= max_price and
                (category == None or menu['category'] == category) and 
                (hot == None or menu['hot'] == hot) and 
                (vegetarian == None or menu['vegetarian'] == vegetarian) and 
                (halal == None or menu['halal'] == halal) and 
                (peanut == None or menu['peanut'] == peanut) and
                (shrimp == None or menu['shrimp'] == shrimp) and
                (lactose == None or menu['lactose'] == lactose)
            )

        menus = Menu.objects.all()
        menus_serialized = MenuSerializer(instance=menus, many=True) 
        # print(menus_serialized.data)
        filtered_menus = list(filter(filter_menu, menus_serialized.data))
        
        # print(filtered_menus)

        if (len(filtered_menus) > 0):
            chosen_menu = random.choice(filtered_menus)
            return Response(chosen_menu, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if (request.method == 'GET'): return get()