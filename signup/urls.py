
from django.urls import path
from . import views


urlpatterns = [
    path("login", views.login_view, name="register"),
    path("accounts", views.signup, name="accounts"),
    path("logout", views.logout_view, name="logout"),

]
