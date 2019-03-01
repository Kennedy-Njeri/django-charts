from django.urls import path
from . import views



urlpatterns = [
    path('', views.ticket_class_view, name="index"),

]