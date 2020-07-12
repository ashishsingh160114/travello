from django.urls import path
from . import views

urlpatterns=[
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("upload", views.upload, name="upload"),
    path("about", views.about, name="about")

]