from django import forms


class TypeSelectionForm(forms.Form):
    type_choices = [('','Select a Pokemon Type'),        
                    ('normal', 'Normal'),
                    ('fighting', 'Fighting'),
                    ('flying', 'Flying'),
                    ('poison', 'Poison'),
                    ('ground', 'Ground'),
                    ('rock', 'Rock'),
                    ('bug', 'Bug'),
                    ('ghost', 'Ghost'),
                    ('steel', 'Steel'),
                    ('fire', 'Fire'),
                    ('water', 'Water'),
                    ('grass', 'Grass'),
                    ('electric', 'Electric'),
                    ('psychic', 'Psychic'),
                    ('ice', 'Ice'),
                    ('dragon', 'Dragon'),
                    ('dark', 'Dark'),
                    ('fairy', 'Fairy'),]
    
    pokemon_type = forms.ChoiceField(choices= type_choices, required=False)

# class SeePokemon(forms.Form):
#     pokemon_choices = [('', 'Select a Pokemon Type')] + fetch_pokemon(pokemon_by_type.api_url)

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=True)