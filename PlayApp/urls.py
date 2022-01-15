from django.urls import path
from PlayApp import views

urlpatterns = [
    path("", views.inicio),
    path("view/", views.primer_view)

]
