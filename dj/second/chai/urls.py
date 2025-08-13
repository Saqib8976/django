from django.urls import path
from .views import *

urlpatterns = [
    path("",form1,name="form1"),
    path("addition/",add,name="add"),

]