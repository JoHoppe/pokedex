from django.urls import path
from . import views

app_name = "pokedexapp"
urlpatterns=[
    #home page
    path("",views.index,name="index"),
    #path for one pokemon
    path('pokemon/<int:id>',views.show_one_pokemon,name="show_one_pokemon"),
    #path for 404
    path('pokemon/404',views.raise_404,name="raise_404"),
    path('pokemon/search',views.search,name="search"),

]