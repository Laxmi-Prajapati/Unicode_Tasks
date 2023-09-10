from django.shortcuts import render


# Create your views here.
import requests
from django.http import JsonResponse

from .forms import TypeSelectionForm
from .models import PokemonCaught
from .forms import SearchForm

def pokemon_types_view(request):
    api_url = "https://pokeapi.co/api/v2/type"

    resp = requests.get(api_url)

    if(resp.status_code == 200):
        data = resp.json()
        types = [entry['name'] for entry in data['results']]

        return JsonResponse({'types' : types})

def default_view(request):
    return render(request, 'default.html')

def pokemon_by_type(request):
    if request.method == 'POST':
        form = TypeSelectionForm(request.POST)
        if form.is_valid():
            selected_type = form.cleaned_data['pokemon_type']
            if selected_type:
                api_url = f"https://pokeapi.co/api/v2/type/{selected_type.lower()}"

                try:
                    response = requests.get(api_url)
                    response.raise_for_status()
                    data = response.json()
                    pokemons = [entry['pokemon']['name'] for entry in data['pokemon']]
                    return render(request, 'pokemon_list.html',{'pokemons':pokemons})
                except requests.exceptions.RequestException as e:
                    error_message = str(e)
                
            else:
                error_message = 'Please select a valid pokemon type'
        
        else:
            error_message = 'Invalid form Data'

    else:
        form = TypeSelectionForm()
        error_message = None


    return render(request, 'type_sel.html',{'form': form, 'error_message': error_message})

def pokemon_search(request):
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            poke = form.cleaned_data['query']
            if poke:
                api_url = f'https://pokeapi.co/api/v2/pokemon/{poke.lower()}'

                resp = requests.get(api_url)
                resp.raise_for_status()
                data = resp.json()

                p, created = PokemonCaught.objects.get_or_create(name = poke)

                moves_data = data.get('moves', [])
                p.moves = [move.get('move', {}).get('name', '') for move in moves_data]
                sprites_data = data.get('sprites',[])
                # p.sprites = [sprite.get('front_default',{}) for sprite in sprites_data]
                if isinstance(sprites_data, dict) and 'front_default' in sprites_data:
                    p.sprites = sprites_data['front_default']
                p.height = data.get('height', 0.0)

                if created:
                    p.level = 1
                else:
                    p.level += 1

                p.save()

                return render(request, 'search_pokemon.html',  {'form': form,'data' : data})
            
        else:
                form = SearchForm()

    return render(request, 'search_pokemon.html', {'form': form})

                    
def caught_pokemon_list(request):
    caught_pokemon = PokemonCaught.objects.all()

    return render(request, 'caught.html',{'caught_pokemon': caught_pokemon})

