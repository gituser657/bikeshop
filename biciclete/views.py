from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# lab 1, cerinta 3, import zile si luni in limba romana, implementare cerinta 3

from datetime import datetime

ZILE = ["Luni", "Marți", "Miercuri", "Joi", "Vineri", "Sâmbătă", "Duminică"]
LUNI = ["", "Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie",
        "Iulie", "August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie"]
def formateaza_data(d):
    return f"{ZILE[d.weekday()]}, {d.day} {LUNI[d.month]} {d.year}"

# laboratorul 1, cerinta 4 metoda Accesare

def get_ip(request):                       # functie din cerinta lab 
    str_lista_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if str_lista_ip:
        return str_lista_ip.split(',')[-1].strip()
    return request.META.get('REMOTE_ADDR')

class Accesare: 
    count = 0       # contor pentru fiecare accesare
    def __init__(self, ip_client, id, url, parametri=None):
        Accesare.count +=1
        self.id = Accesare.count
        self.ip_client = ip_client
        self.url = url
        self.parametri = parametri if parametri is not None else {}
        self.data = datetime.now()  # moment creare
    
    #lab 1, ex 5 - metoda lista_parametri()
    
    def lista_parametri(self):
        return [(nume, valoare if valoare != "" else None)
                for nume, valoare in self.parametri.items()]
accesari = []


def index(request):
    accesari.append(Accesare(get_ip(request), request.get_full_path(), request.GET.dict()))  # lab 1, ex 4 apelare functie accesari
    # variabila pentru text lung 
    # title afiseaza numele in tab-ul din browser
    descriere=""" 
    <title>BikeMania.ro</title> 
    <h1>Magazin biciclete</h1>                 
    <p> Magazin online pentru biciclete de oras si de munte, plus accesorii si piese de schimb.</p>
    <p> Clientii pot filtra dupa categorie &amp; brand. </p> 
    """
    return HttpResponse(descriere)

# lab 1, cerinta 2, pagina info cu H1
def info(request): 
    # accesari.append(Accesare(get_ip(request), request.get_full_path(), request.GET.dict())) # lab 1, ex 4 apelare functie accesari
    # salvare in variabila accesare. ex5 
    
    accesare = Accesare(get_ip(request), request.get_full_path(), request.GET.dict())
    accesari.append(accesare)
    print(accesare.lista_parametri)
    
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