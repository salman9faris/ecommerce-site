from django.shortcuts import render
from .models import Item


from django.contrib.auth.decorators import login_required



def home(request):
    item = Item.objects.all()

    context = {
        'item': item
    }
    return render(request, "index.html", context)



def fruits(request):
    item = Item.objects.filter(category='f')
    context = {
        'item': item
    }
    return render(request, "shop.html", context)



def vegetables(request):
        item = Item.objects.filter(category='v')
        context = {
            'item': item
        }
        return render(request, "shop.html", context)



def juice(request):
    item = Item.objects.filter(category='j')
    context = {
        'item': item
    }
    return render(request, "shop.html", context)

def shop(request):
    item = Item.objects.all()
    context = {
        'item': item
    }
    return render(request, "shop.html", context)


@login_required(login_url="register")
def wishlist(request):
    return render(request, "wishlist.html")


@login_required(login_url = "register" )
def contactus(request):
    return render(request, "contact.html")




