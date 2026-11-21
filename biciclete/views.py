from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):

    # variabila pentru text lung 
    # title afiseaza numele in tab-ul din browser
    descriere=""" 
    <title>BikeMania.ro</title> 
    <h1>Magazin biciclete</h1>                 
    <p> Magazin online pentru biciclete de oras si de munte, plus accesorii si piese de schimb.</p>
    <p> Clientii pot filtra dupa categorie &amp brand. </p> 
    """
    return HttpResponse(descriere)

# lab 1, cerinta 3, import zile si luni in limba romana, implementare cerinta 3

from datetime import datetime

ZILE = ["Luni", "Marți", "Miercuri", "Joi", "Vineri", "Sâmbătă", "Duminică"]
LUNI = ["", "Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie",
        "Iulie", "August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie"]
def formateaza_data(d):
    return f"{ZILE[d.weekday()]}, {d.day} {LUNI[d.month]} {d.year}"

# lab 1, cerinta 2, pagina info cu H1
def info(request): 
    acum = datetime.now()
    info_descriere = f"""
    <!DOCTYPE html>
    <html lang="ro">
    <head>
        <meta charset="utf-8">
        <title>Informații despre server</title>
    </head>
    <body>
        <h1>Informații despre server</h1>    
    <section>
        <h2>Data și ora</h2>
        <p>{formateaza_data(acum)}, ora {acum.strftime('%H:%M:%S')}</p>
    </section>
    </body>
    </html>"""
    return HttpResponse(info_descriere)
