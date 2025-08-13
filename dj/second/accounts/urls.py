from django.urls import path
from .views import *

urlpatterns = [
    path("register/",register,name="register"),
    path("login/",Login,name="login"),
    path("logout/",logout,name="logout"),


]