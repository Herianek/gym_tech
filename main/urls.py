from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path("ceny",views.ceny, name="ceny"),
    path("food",views.food, name="food"),
    path("training",views.training, name="training"),
    path("formy",views.formy, name="formy"),
    path("<int:id>",views.food_user, name="food_user"),
    path("onas",views.onas, name="onas"),
    path("zaregistrujse",views.zaregistrujse, name="zaregistrujse"),
]
