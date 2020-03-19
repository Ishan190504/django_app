from django.urls import path
from . import views
urlpatterns = [
    path("<int:id>/", views.index, name="index"),
    path("home/", views.home, name="homie"),
    path("", views.default, name="home page"),
    path("create/", views.create, name="create"),
    path("logout/", views.logout, name="log out"),
    path("view/", views.views, name="views"),

]