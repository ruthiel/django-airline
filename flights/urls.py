from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.auth_login, name="login"),
    path("logout", views.auth_logout, name="logout"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book")
]