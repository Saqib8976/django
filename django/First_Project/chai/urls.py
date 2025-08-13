from django.urls import path
from .views import *

urlpatterns = [
    path('', all_chai, name='all_chai')

]
