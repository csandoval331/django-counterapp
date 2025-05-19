from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addusername", views.addusername, name="addusername"),
    path("removeusername/<int:username>", views.removeusername, name="removeusername")

]