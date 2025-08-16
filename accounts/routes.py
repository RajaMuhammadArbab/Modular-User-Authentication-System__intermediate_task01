from django.urls import path
from . import controllers as ctrl

urlpatterns = [
    path("register", ctrl.register, name="register"),
    path("login", ctrl.login, name="login"),
    path("logout", ctrl.logout, name="logout"),
]
