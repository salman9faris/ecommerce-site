from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from item import item

from esite.models import Item
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required


class Cart(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            print(item)
            context = {
                'item': order
            }
            return render(self.request, 'cart.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("shop")


@login_required(login_url="register")
def add_to_cart(request, id):
    item = get_object_or_404(Item, id=id)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__id=item.id).exists():
            order_item.quantity = F('quantity') + 1
            order_item.save()
            messages.success(request, str(item).lower() + " quantity was updated.")
            return redirect("shop")
        else:
            order.items.add(order_item)
            messages.success(request, str(item).lower() + " added to your cart1")
            return redirect("shop")
    else:
        order = Order.objects.create(
            user=request.user)
        order.items.add(order_item)
        messages.success(request, str(item).lower() + " added to your cart")
        return redirect("shop")


@login_required
def remove_from_cart(request, id):
    item = get_object_or_404(Item, id=id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, str(item).lower() + " was removed from your cart.")
            return redirect("cart")


@login_required
def remove_single_item_from_cart(request, id):
    item = get_object_or_404(Item, id=id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, str(item).lower() + " item quantity was updated")
            return redirect("cart")

@login_required
def add_single_item_to_cart(request, id):
    item = get_object_or_404(Item, id=id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 0:
                order_item.quantity += 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, str(item).lower() + " item quantity was updated")
            return redirect("cart")
