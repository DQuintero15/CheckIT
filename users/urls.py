from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("signUp", views.signUp, name="signUp"),
    path("sign-client", views.signUpClient, name="signUpClient"),
]
