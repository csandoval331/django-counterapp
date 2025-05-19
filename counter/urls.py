from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("down", views.down, name="down"),
    path("up", views.up, name="up"),
    path("reset", views.reset, name="reset"),

]