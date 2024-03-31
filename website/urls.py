from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("about", views.about),
    path("boardpage", views.boardpage),
    path("events", views.events),
    path("homepage", views.homepage),
    path("membership", views.membership),
    path("register", views.register),
    path("sponsorship", views.sponsorship)
]