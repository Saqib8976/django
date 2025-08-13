from django.urls import path
from .views import *

urlpatterns = [
    path("", hellofunc, name="hellofunc"),
    path("add",add,name='add'),

]
