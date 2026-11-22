from django.urls import path, re_path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("info", views.info, name="info"), #lab 1, cerinta 2
    path("log", views.log, name="log"), #lab 2, cerinta 1 din task 1
    path("istoric", views.istoric, name="istoric"),
    path("despre", views.despre, name="despre"),
    re_path(r"^accesare(?P<id_accesare>\d+)$", views.detalii_accesare, name="detalii_accesare"),
]   