
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("wish_list", views.wishlist, name="wishlist"),
    path("shop", views.shop, name="shop"),
    path("contactus", views.contactus, name="contactus"),
    path("fruits", views.fruits, name="fruits"),
    path("vegetables", views.vegetables, name="vegetables"),
    path("juice", views.juice, name="juice"),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
