from django.urls import path
from . import views

urlpatterns = [
    path("registro/", views.registro, name="registro"),
    path("login/", views.LoginUsuarioView.as_view(), name="login"),
    path("logout/", views.logout_usuario, name="logout"),
]