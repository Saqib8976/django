from django.shortcuts import render
from .models import *

# Create your views here.


def travelo(request):

    # dest1 = Destination()
    # dest1.name = "Mumbai"
    # dest1.desc = "city that never sleeps... "
    # dest1.img = "destination_1.jpg"
    # dest1.price = 600
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.name = "Lucknow"
    # dest2.desc = "city for nawaabs...!"
    # dest2.img = "destination_2.jpg"
    # dest2.price = 400
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.name = "Hydrabad"
    # dest3.desc = "city for mughals..."
    # dest3.img = "destination_3.jpg"
    # dest3.price = 500
    # dest3.offer = False

    # dests = [dest1, dest2, dest3]
    dests = Destination.objects.all()

    return render(request, "index.html", {"dests": dests})
