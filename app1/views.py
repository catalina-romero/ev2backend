from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'templates_app1\index.html')

def electronica(request):
    data={
        "titulo":"Electrónica",
        'producto1':"MAC",
        'producto2':"Celular",
        'producto3':"PlayStation",
        'imagen':'images/producto.jpg'
    }
    return render(request,'templates_app1/productos.html',data)

def juguetes(request):
    data={
        "titulo":"Juguetes",
        'producto1':"Pelota",
        'producto2':"Muñeca",
        'producto3':"Carro",
        'imagen':'images/producto.jpg'
    }
    return render(request,'templates_app1/productos.html',data)

def ropa(request):
    data={
        "titulo":"Ropa",
        'producto1':"Camisa",
        'producto2':"Pantalon",
        'producto3':"Zapatos",
        'imagen':'images/producto.jpg'
    }
    return render(request,'templates_app1/productos.html',data)
