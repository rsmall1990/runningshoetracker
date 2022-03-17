from django.shortcuts import render
from django.http import HttpResponse

"""
Fake data
"""

class shoe:
    def __init__(self, brand, color, miles):
        self.brand = brand
        self.color = color
        self.miles = miles

shoes = [
    shoe('nikes', 'black', 200),
    shoe('brooks', 'orange', 150)
]

# Create your views here.

def home(request):
    return render(request, 'home.html', )

def about(request):
    return render(request, 'about.html', )

def shoes_index(request):
    return render(request, 'shoes/index.html', {'shoes': shoes})