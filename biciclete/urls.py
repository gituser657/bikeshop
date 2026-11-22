from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("info", views.info, name="info"), #lab 1, cerinta 2
    path("log", views.log, name="log"), #lab 2, cerinta 1 din task 1
]   