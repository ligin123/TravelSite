from django.shortcuts import render

# Create your views here.
from .models import Place, Person


def demo(request):
    obj = Place.objects.all()
    obj1 = Person.objects.all()
    return render(request, "index.html", dict(result=obj, person=obj1))


def about(request):
    return render(request, "about.html")
