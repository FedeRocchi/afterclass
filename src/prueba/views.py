from django.shortcuts import render

# Create your views here.


def index(request):
    nombre = input("Dime tu nombre: ")
    apellido = input("Apellido: ")
    año = 2024
    datos = {
        "nombre": nombre,
        "apellido": apellido,
        "año": año,
    }
    return render(request, "prueba/index.html", datos)
