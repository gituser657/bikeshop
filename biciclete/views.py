from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# lab 1, cerinta 3, import zile si luni in limba romana, implementare cerinta 3

#lab 1, ex 6 - import urls
from urllib.parse import urlparse

from datetime import datetime

#lab 1, exercitiu 7 calculeaza_data()
#setare format implicit
# %A -- ziua 
# %B -- luna 
# %-d --elimina 0-urile din data ex 02 nov - devine 2 nov. 
# %Y -- an


# lab 2, ex 4 - task 1 
# definire proprietati pentru tabel cu vizibilitate globala


PROPRIETATI = ["id", "ip_client", "url", "parametri", "data"]
FORMAT_IMPLICIT = "%A, %-d %B %Y" 

ZILE = ["Luni", "Marți", "Miercuri", "Joi", "Vineri", "Sâmbătă", "Duminică"]
LUNI = ["", "Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie",
        "Iulie", "August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie"]
def formateaza_data(d, format=FORMAT_IMPLICIT):

# comnetare implementare lab 1, cerinta 3 
#    return f"{ZILE[d.weekday()]}, {d.day} {LUNI[d.month]} {d.year}"

# implementare format nou, lab 1, cerinta 7

    format = format.replace("%A", ZILE[d.weekday()])
    format = format.replace("%B", LUNI[d.month])
    format = format.replace("%-d", str(d.day))
    return d.strftime(format)

# final implementare format nou, lab 1, cerinta 7


# laboratorul 1, cerinta 4 metoda Accesare


# block get_ip comentat in urma implementarii cerintei 8 din lab 1
# middleware.py 


# def get_ip(request):                       # functie din cerinta lab 1, ex 4
#     str_lista_ip = request.META.get('HTTP_X_FORWARDED_FOR')
#     if str_lista_ip:
#         return str_lista_ip.split(',')[-1].strip()
#     return request.META.get('REMOTE_ADDR')

class Accesare: 
    count = 0    # contor pentru fiecare accesare
    PREFIX = "/biciclete" # lab 1, ex 6 
    def __init__(self, ip_client, url, parametri=None):
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
    
    #lab 1, ex 6 -- metodele string_url() & pagina()
    def string_url(self):
        return self.url
    
    def pagina(self):
        cale =urlparse(self.url).path
        return cale.removeprefix(Accesare.PREFIX) or "/"
    
    # lab 1, ex 7 - definire metoda calculeaza_data, cu setare format implicit definit mai sus
    # def calculeaza_data(self, format=FORMAT_IMPLICIT):
    #     return formateaza_data(self.data, format)
        
    # implementare lab 1, ex 10 - in formateaza_data se adauga un al 3-lea parametru numit, tip
    
    def calculeaza_data(self, format=FORMAT_IMPLICIT, tip=""):
        if tip == "zi":
            text = formateaza_data(self.data, FORMAT_IMPLICIT)
        elif tip == "timp":
            text = self.data.strftime("%H:%M:%S")
        else:
            text = formateaza_data(self.data, format) + ", ora " + self.data.strftime("%H:%M:%S")
        return f"<section><h2>Data și ora</h2><p>{text}</p></section>"

    
    # lab 1, ex 9 - metoda _str_ 
    
    def __str__(self):
        return (f"id: {self.id}\n"
                f"ip_client: {self.ip_client}\n"
                f"string_url: {self.string_url()}\n"
                f"pagina: {self.pagina()}\n"
                f"calculeaza_data: {self.calculeaza_data()}\n"
                f"lista_parametri: {self.lista_parametri()}")
    
accesari = []


def index(request):
    # accesari.append(Accesare(get_ip(request), request.get_full_path(), request.GET.dict())) # lab 1, ex 4 apelare functie accesari
    
    #modificare in request.build_absolute_uri() - lab 1, ex 6
    
    # accesari.append(Accesare(request.ip_client, request.build_absolute_uri(), request.GET.dict()))
    accesare =Accesare(request.ip_client, request.build_absolute_uri(), request.GET.dict())
    accesari.append(accesare)    
    # variabila pentru text lung 
    # title afiseaza numele in tab-ul din browser
    descriere=""" 
    <title>BikeMania.ro</title> 
    <h1>Magazin biciclete</h1>                 
    <p> Magazin online pentru biciclete de oras si de munte, plus accesorii si piese de schimb.</p>
    <p> Clientii pot filtra dupa categorie &amp; brand. </p> 
    """
    print(accesare)
    return HttpResponse(descriere)

# lab 1, cerinta 2, pagina info cu H1
def info(request): 
    # accesari.append(Accesare(get_ip(request), request.get_full_path(), request.GET.dict())) # lab 1, ex 4 apelare functie accesari
    # salvare in variabila accesare. ex5 
    
    # accesare = Accesare(get_ip(request), request.get_full_path(), request.GET.dict())
    
    accesare = Accesare(request.ip_client, request.build_absolute_uri(), request.GET.dict())
    accesari.append(accesare)
    tip = accesare.parametri.get("data","")
    sectiune = accesare.calculeaza_data(tip=tip)
    
    # print(accesare.lista_parametri())
    # print(accesare.string_url(), accesare.pagina())

    
    # verificare ca middleware-ul creat functioneaza - ex 8
    # print(accesare.ip_client)
    
    # test metoda _str_ -- ex 9, lab 1
    print (accesare)
    # eliminare functie datetime.now() & folosire metoda accesare.calculeaza_data()
    # acum = datetime.now()
    
    # lab 1, ex 10 - modificare paramtru sectiune 
    
    info_descriere = ("""
    <!DOCTYPE html>
    <html lang="ro">
    <head>
        <meta charset="utf-8">
        <title>Informații despre server</title>
    </head>
    <body>
        <h1>Informații despre server</h1>    
    """ 
    + 
    sectiune 
    +
    """
    </body>
    </html>""")
    return HttpResponse(info_descriere)



# lab 2, cerinta 1 din task 1 -- definire pagina /log
# se va testa prin localhost:8000/biciclete/log?ultimele= --> insert nr 

def log(request):
    accesare = Accesare(request.ip_client, request.build_absolute_uri(), request.GET.dict())
    accesari.append(accesare)
    print(accesare)

    selectate = accesari
    mesaj = ""
    ultimele = request.GET.get("ultimele")
    
    # verificare valoare accesari, inclusiv nr negativ trimis ca parametru 
    
    if ultimele is not None:
        try:
            n = int(ultimele)
            if n < 1:
                raise ValueError
            if n > len(accesari):
                mesaj = f"<p>Exista doar {len(accesari)} accesari fata de {n} accesari cerute</p>"
            else:
                selectate = accesari[-n:]
        except ValueError:
            selectate = []
            mesaj = "<p>Parametrul ultimele trebuie sa fie un numar intreg pozitiv.</p>"
    
    # lab 2, ex2 - task 1  parametrii iduri si dubluri
    valori_iduri = request.GET.getlist("iduri")       # ex: ["2,3", "5", "4,2,1"]
    if valori_iduri:
        dubluri = request.GET.get("dubluri", "false") == "true"

        # toate id-urile intr-o singura lista de numere
        lista_iduri = []
        try:
            for valoare in valori_iduri:
                for bucata in valoare.split(","):
                    lista_iduri.append(int(bucata))
        except ValueError:
            lista_iduri = []
            mesaj = mesaj + "<p>Parametrul iduri trebuie sa contina doar numere separate prin virgula.</p>"

        # eliminare dubluri (daca dubluri e false), pastrand ordinea
        if not dubluri:
            fara_dubluri = []
            for i in lista_iduri:
                if i not in fara_dubluri:
                    fara_dubluri.append(i)
            lista_iduri = fara_dubluri

        # cauta accesarile cu id-urile cerute
        selectate = []
        for i in lista_iduri:
            for a in accesari:
                if a.id == i:
                    selectate.append(a)
    
        # parametrul accesari=nr
        # sectiune_nr = ""
        # if request.GET.get("accesari") == "nr":
        #     sectiune_nr = f"<section><h2>Număr accesări</h2><p>{len(accesari)}</p></section>"
        
    # lab 2, task 1 - ex 3 - implementare accesari detalii 
    sectiune_accesari = ""
    if request.GET.get("accesari") == "nr":
        sectiune_accesari = f"<section><h2>Număr accesări</h2><p>{len(accesari)}</p></section>"
    elif request.GET.get("accesari") == "detalii":
        elemente_detalii = ""
        for a in accesari:
            elemente_detalii = elemente_detalii + f"<li>{formateaza_data(a.data)}, ora {a.data.strftime('%H:%M:%S')}</li>"
        sectiune_accesari = "<section><h2>Detalii accesări</h2><ul>" + elemente_detalii + "</ul></section>"
    
    # final implementare lab 2, ex 2 - task 1 - parametrizare /log nu id-uri
    
    # lista elemente 
    elemente = "".join(
        f"<li>{a.id} | {a.pagina()} | {a.string_url()} | {formateaza_data(a.data)}, ora {a.data.strftime('%H:%M:%S')}</li>"
        for a in selectate
    )
    
    # sectiune parametri 
    
    nume_parametri = list(request.GET.keys())
    elemente_parametri = ""
    for nume in nume_parametri:
        elemente_parametri = elemente_parametri + f"<li>{nume}</li>"
    sectiune_parametri = (f"<section><h2>Parametri</h2><p>Număr parametri: {len(nume_parametri)}</p>"
                "<ul>" + elemente_parametri + "</ul></section>")
        

    # parametrul tabel
    continut = "<ul>" + elemente + "</ul>"            # implicit: lista
    tabel = request.GET.get("tabel")
    if tabel:
        if tabel == "tot":
            coloane = PROPRIETATI
        else:
            coloane = []
            for nume in tabel.split(","):
                nume = nume.strip()
                if nume in PROPRIETATI:
                    coloane.append(nume)
                else:
                    mesaj = mesaj + f"<p>Proprietatea {nume} nu exista.</p>"

        antet = ""
        for c in coloane:
            antet = antet + f"<th>{c}</th>"

        randuri = ""
        for a in selectate:
            celule = ""
            for c in coloane:
                valoare = getattr(a, c)
                if c == "data":
                    valoare = formateaza_data(valoare) + ", ora " + valoare.strftime("%H:%M:%S")
                celule = celule + f"<td>{valoare}</td>"
            randuri = randuri + f"<tr>{celule}</tr>"

        continut = f'<table border="1"><tr>{antet}</tr>{randuri}</table>'
    
    pagina = ("""<!DOCTYPE html>
        <html lang="ro">
        <head><meta charset="utf-8"><title>Log accesări</title></head>
        <body>
            <h1>Log accesări</h1>
            """ + continut + mesaj + sectiune_accesari + sectiune_parametri + """
        </body>
        </html>""")
    return HttpResponse(pagina)



