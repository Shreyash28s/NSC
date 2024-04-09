from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("about", views.about, name="about"),
    path("boardpage", views.boardpage, name ="boardpage"),
    path("events", views.events, name="events"),
    path("homepage", views.homepage, name="home"),
    path("membership", views.membership, name="membership"),
    path("register", views.register),
    path("sponsorship", views.sponsorship, name="sponsorship")
]