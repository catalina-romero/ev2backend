from django.shortcuts import render

# Create your views here.
def estaciones(request):
    data = {
        "titulo":"Estaciones",
        'estacion1':"Verano",
        'estacion2':"Otoño",
        'estacion3':"Invierno",
        'estacion4':"Primavera",
        'url1': '/verano',
        'url2': '/otono',
        'url3': '/invierno',
        'url4': '/primavera',
        'imagen':'images/estaciones.jpg',
        'item1':'',
        'item2':'',
        'item3':'',
        'item4':'',
        'item5':'',
    }
    return render(request, 'templates_app2/solo.html', data)

def verano(request):
    data = {
        "titulo":"Verano",
        'estacion1':"Estaciones",
        'estacion2':"Otoño",
        'estacion3':"Invierno",
        'estacion4':"Primavera",
        'url1': '/',
        'url2': '/otono',
        'url3': '/invierno',
        'url4': '/primavera',
        'imagen':'images/verano.jpg',
        'item1':'Durante el solsticio de verano el día es más largo y la noche más corta del año.',
        'item2':'Se presentan las temperaturas promedios más elevadas.',
        'item3':'Es la época más seca del año en las zonas alejadas de los trópicos.',
        'item4':'Generalmente es la época de vacaciones escolares.',
        'item5':'Hay un mayor crecimiento de la flora y mayor actividad de la fauna.',
        
    }
    return render(request, 'templates_app2/solo.html', data)

def otono(request):
    data = {
        "titulo":"Otoño",
        'estacion1':"Verano",
        'estacion2':"Estaciones",
        'estacion3':"Invierno",
        'estacion4':"Primavera",
        'url1': '/verano',
        'url2': '/',
        'url3': '/invierno',
        'url4': '/primavera',
        'imagen':'images/otono.jpg',
        'item1':'Las temperaturas comienzan a bajar.',
        'item2':'Los días se acortan y las noches se alargan.',
        'item3':'La coloración de las hojas de los árboles adquiere tonos rojizos y amarillos, y caen de las ramas.',
        'item4':'La fauna se prepara para el invierno, inicia una época de reproducción y migración de especies.',
        'item5':'',
        
    }
    return render(request, 'templates_app2/solo.html', data)

def invierno(request):
    data = {
        "titulo":"Invierno",
        'estacion1':"Verano",
        'estacion2':"Otoño",
        'estacion3':"Estaciones",
        'estacion4':"Primavera",
        'url1': '/verano',
        'url2': '/otono',
        'url3': '/',
        'url4': '/primavera',
        'imagen':'images/invierno.jpg',
        'item1':'Presenta las temperaturas más bajas del año en el hemisferio específico.',
        'item2':'El día tiene menor duración y las noches son más largas.',
        'item3':'Es común que, en las zonas alejadas de los trópicos y más cercanas a los polos, se de la caída de nieve.',
        'item4':'Los árboles presentan menos follaje y las plantas tienen menos actividad.',
        'item5':'Muchos animales se encuentran en hibernación, en gestación y han emigrado a zonas más cálidas.',
    }
    return render(request, 'templates_app2/solo.html', data)

def primavera(request):
    data = {
        "titulo":"Primavera",
        'estacion1':"Verano",
        'estacion2':"Otoño",
        'estacion3':"Invierno",
        'estacion4':"Estaciones",
        'url1': '/verano',
        'url2': '/otono',
        'url3': '/invierno',
        'url4': '/',
        'imagen':'images/primavera.jpg',
        'item1':'Las temperaturas comienzan a elevarse.',
        'item2':'Los días se hacen más largos y las noches se acortan.',
        'item3':'Es una época generalmente húmeda y con presencia de tormentas.',
        'item4':'Las plantas y árboles comienzan a activarse y a dar flores.',
        'item5':'La fauna sale de sus escondites, deja de hibernar o retorna como parte de sus ciclos migratorios.',
    }
    return render(request, 'templates_app2/solo.html', data)