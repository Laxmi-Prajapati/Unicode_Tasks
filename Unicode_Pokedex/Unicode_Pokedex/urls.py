"""
URL configuration for Unicode_Pokedex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pokedex_app import views
from pokedex_app.views import pokemon_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemon-types/', views.pokemon_types_view, name='pokemon_types_view'),
    path('', views.default_view, name='default_view'),
    path('by_type/', views.pokemon_by_type, name='pokemon_by_type'),
    path('pokemon_search/', views.pokemon_search, name='pokemon_search'),
    path('caught_pokemon/', views.caught_pokemon_list, name='caught_pokemon_list')
]

